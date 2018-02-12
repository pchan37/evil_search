from utils import utils


class Searcher(object):

    def __init__(self, input_string, regex):
        self.input_string = input_string
        self.regex_pattern = regex

    def search_once(self, start_index, end_index=float('inf')):
        search_list = []

        if start_index < 0:
            return search_list

        match = self.regex_pattern.search(self.input_string, start_index)
        if match is not None and match.start() < end_index:
            search_list = (match.group(0), str(match.start()))
        return search_list

    def search_all(self, start_index, end_index=float('inf')):
        list_of_searches = []

        search_list = self.search_once(start_index, end_index)
        while search_list:
            match_start = int(search_list[1])
            if search_list in list_of_searches or match_start >= end_index:
                break
            else:
                list_of_searches.append(search_list)
            start_index = match_start + 1
            search_list = self.search_once(start_index, end_index)
        return utils.unpack_inner_lists_in_list(list_of_searches)
