import utils


class Searcher(object):

    def __init__(self, input_string, regex):
        self.input_string = input_string
        self.regex_pattern = regex

    def search_once(self, start_index, end_index=float('inf')):
        search_tuple = ()

        if start_index < 0:
            return search_tuple

        match = self.regex_pattern.search(self.input_string, start_index)
        if match is not None and match.start() < end_index:
            search_tuple = (match.group(0), str(match.start()))
        return search_tuple

    def search_all(self, start_index, end_index=float('inf')):
        search_match_list = []

        search_match_tuple = self.search_once(start_index, end_index)
        while search_match_tuple:
            match_start = int(search_match_tuple)
            if search_match_tuple in search_match_list or match_start >= end_index:
                break
            else:
                search_match_list.append(search_match_tuple)
            start_index = match_start + 1
            search_match_tuple = self.search_once(start_index, end_index)
        return utils.unpack_tuple_in_list(search_match_list)
