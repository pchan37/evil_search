import Searcher
from utils import utils


class Replacer(object):

    def __init__(self, input_string, regex, replacement):
        self.input_string = input_string
        self.regex_pattern = regex
        self.replacement = replacement
        self.searcher = Searcher.Searcher(input_string, regex)

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

        list_of_replacements_no_overlap = []
        for index, replacements in enumerate(list_of_replacements):
            if index > 0:
                if int(replacements[2]) >= int(list_of_replacements[index - 1][2]) + len(list_of_replacements[index - 1][0]):
                    list_of_replacements_no_overlap.append(replacements)
            else:
                list_of_replacements_no_overlap.append(replacements)

        return utils.unpack_inner_lists_in_list(list_of_replacements_no_overlap)
