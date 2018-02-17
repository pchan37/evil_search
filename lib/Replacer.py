import Searcher
from utils import utils


class Replacer(object):

    def __init__(self, input_string, regex, replacement):
        self.regex_pattern = regex
        self.replacement = replacement
        self.searcher = Searcher.Searcher(input_string, regex)

    def get_replacement_attr(self, replacement_list):
        return len(replacement_list[0]), len(replacement_list[1]), int(replacement_list[2])

    def adjust_for_overlap(self, list_of_replacements):
        if not list_of_replacements:
            return list_of_replacements

        first_elem = list_of_replacements[0]
        list_of_replacements_no_overlap = [first_elem]
        search_len, replace_len, start = self.get_replacement_attr(first_elem)
        previous_match_length = start + search_len
        offset = search_len - replace_len

        for replacements in list_of_replacements[1:]:
            if int(replacements[2]) >= previous_match_length:
                old_replacements = replacements[:]
                replacements[2] = str(int(replacements[2]) - offset)
                list_of_replacements_no_overlap.append(replacements)

                search_len, replace_len, start = self.get_replacement_attr(old_replacements)
                previous_match_length = start + search_len
                offset += (search_len - replace_len)
        return list_of_replacements_no_overlap

    def replace_once(self, start_index, end_index=float('inf')):
        replacement_list = []

        search_list = self.searcher.search_once(start_index, end_index)
        match_start = int(search_list[1]) if search_list else None
        if search_list and match_start < end_index:
            substitute_result = self.regex_pattern.sub(self.replacement, search_list[0], count=1)
            replacement_list = [search_list[0], substitute_result, search_list[1]]
        return replacement_list

    def replace_all(self, start_index, end_index=float('inf')):
        list_of_replacements = []

        replacement_list = self.replace_once(start_index, end_index)
        while replacement_list:
            match_start = int(replacement_list[2])
            if replacement_list in list_of_replacements or match_start >= end_index:
                break
            else:
                list_of_replacements.append(replacement_list)
            start_index = match_start + 1
            replacement_list = self.replace_once(start_index, end_index)

        list_of_replacements_no_overlap = self.adjust_for_overlap(list_of_replacements)
        return utils.unpack_inner_lists_in_list(list_of_replacements_no_overlap)
