;;; evil-search.el --- Searching and replacing with vim-like syntax

;; Package-Requires: ((dash "2.13.0"))

;;; Commentary:

;;; Code:

(require 'dash)

(defvar evil-search-python-command
  (concat (format "python %s "
                  (expand-file-name "evil_search.py"
                                    (file-name-directory load-file-name)))
          "%s %s %s")
  "Command to execute.")

(defun evil-search-run-python-command (buffer-content regex point-index)
  "Execute `evil-search-python-command' passing it BUFFER-CONTENT, REGEX, and POINT-INDEX."
  (interactive)
  (replace-regexp-in-string "\n$" "" (shell-command-to-string
                                      (format evil-search-python-command
                                              (shell-quote-argument buffer-content)
                                              (shell-quote-argument regex)
                                              (number-to-string point-index)))))

(defun get-last-index (string substring-to-search &optional start-index)
  "Search STRING for index of the last occurrence of SUBSTRING-TO-SEARCH and return it."
  (interactive)
  (let ((start-index (or start-index (- (length string) (length substring-to-search)))))
    (cond
     ((< start-index 0) -1)
     ((string-match substring-to-search string start-index) start-index)
     (t (get-last-index string substring-to-search (1- start-index))))))

(defun python-string-to-elisp-list (python-string)
  "Convert PYTHON-STRING into an Elisp list."
  (let ((base64-encoded-list (split-string python-string ", ")))
    (--map-indexed (or (and (= (mod (1+ it-index) 3) 0)
                            (string-to-number (base64-decode-string (substring it 1 -1))))
                       (base64-decode-string (substring it 1 -1)))
                   base64-encoded-list)))

(defun get-relevant-data-from-python-command-result (command-output)
  "Get search/replace result and regex flags from COMMAND-OUTPUT."
  (let* ((search-replace-result-end-index (get-last-index command-output ","))
         (raw-search-replace-result (substring command-output
                                               2
                                               (1- search-replace-result-end-index)))
         (search-replace-result
          (python-string-to-elisp-list raw-search-replace-result))
         (regex-flags (substring command-output
                                 (+ search-replace-result-end-index 3)
                                 (get-last-index command-output "'"))))
    (list search-replace-result regex-flags)))

(defun get-user-input (user-input-prompt allowable-chars-regex)
  "Prompt user with USER-INPUT-PROMPT for a char that is matched by ALLOWABLE-CHARS-REGEX."
  (let ((user-input))
    (while (or (not user-input)
               (not (numberp (string-match-p allowable-chars-regex (char-to-string user-input)))))
      (setq user-input (read-char user-input-prompt)))
    user-input))

(defun evil-search-display (index search-result)
  "Move point to the position specified by INDEX in SEARCH-RESULT."
  ;; Add one to account for minimum point being 1
  (goto-char (1+ (nth index search-result))))

(defun evil-search (search-result regex-flags)
  "Search base on data in SEARCH-RESULT and REGEX-FLAGS modifiers."
  (let ((original-point (point))
        (index 0)
        (max-index (length search-result))
        (user-input))
    (evil-search-display (1+ index) search-result)
    (while (or (not user-input) (not (char-equal user-input ?q)))
      (setq user-input
            (get-user-input "p for prev, n for next, q to stop, o for original pos: " "[pnqo]"))
      (cond ((char-equal user-input ?p) (progn
                                          (setq index (mod (- index 2) max-index))
                                          (evil-search-display (1+ index) search-result)))
            ((char-equal user-input ?n) (progn
                                          (setq index (mod (+ index 2) max-index))
                                          (evil-search-display (1+ index) search-result)))
            ((char-equal user-input ?o) (progn
                                          (goto-char original-point)
                                          (setq user-input ?q)))
            ((char-equal user-input ?q) nil)))))

(defun evil-substitute-make-replacement (string-to-search replacement-string &optional query-p)
  "Replace STRING-TO-SEARCH with REPLACEMENT-STRING, querying user if QUERY-P."
  (if query-p
      (progn
        (let* ((prompt-string (format "Do you want to replace %s with %s [y/n]? "
                                      string-to-search
                                      replacement-string))
               (user-input (get-user-input prompt-string "[yn]")))
          (cond
           ((char-equal user-input ?y)
            (perform-replace string-to-search replacement-string nil nil nil 1))
           ((char-equal user-input ?n) nil))))
    (perform-replace string-to-search replacement-string nil nil nil 1)))

(defun evil-substitute (replace-result regex-flags)
  "Substitute base on data in REPLACE-RESULT and REGEX-FLAGS modifiers."
  (save-excursion
    (let* ((index 0)
           (max-index (length replace-result))

           (string-to-search)
           (replacement-string)
           (start-search-index)

           (query-p (numberp (string-match "c" regex-flags))))
      (let ((inhibit-redisplay (not query-p)))
        (while (<= (+ index 3) max-index)
          (setq string-to-search (nth index replace-result)
                replacement-string (nth (1+ index) replace-result)
                start-search-index (nth (+ index 2) replace-result))
          (goto-char (1+ start-search-index))
          (evil-substitute-make-replacement string-to-search replacement-string query-p)
          (setq index (+ index 3))))
      (if query-p
          (message "Done!")
        (message "Success, replaced %s occurrences!" (/ max-index 3)))
      (sit-for 1))))

(defun evil-search-and-substitute (&optional input)
  "Perform evil-search or evil-substitute based on user input or optional arg, INPUT."
  (interactive)
  (let* ((input (or input (read-string "")))
         (py-command-output (evil-search-run-python-command (buffer-string) input (1- (point))))
         (relevant-data (get-relevant-data-from-python-command-result py-command-output))
         (search-replace-result (car relevant-data))
         (regex-flags (car (cdr relevant-data))))
    (cond
     ((null search-replace-result) (progn (message "Search failure...")
                                          (sit-for 1)))
     ((string-prefix-p "/" input) (evil-search search-replace-result regex-flags))
     ((string-prefix-p "s" input) (evil-substitute search-replace-result regex-flags))
     (t (message "Wrong format!")))))

(provide 'evil-search)
;;; evil-search.el ends here
