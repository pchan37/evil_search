# import mypy
import re
import sys

from lib import Replacer
from lib import Searcher


def evil_search(start, buffer_string, string_to_search, flags=''):
    # type: (int, str, str, mypy.typing.Optional[str]) -> mypy.Any
    re_flags = re.MULTILINE
    if 'i' in flags:
        re_flags |= re.IGNORECASE
    regex = re.compile(string_to_search, flags=re_flags)
    searcher = Searcher.Searcher(buffer_string, regex)
    search_match_list = []  # type: list
    search_match_list.extend(searcher.search_all(start))
    search_match_list.extend(searcher.search_all(0, end_index=start))
    return (search_match_list, flags)


def evil_substitute(start, buffer_string, string_to_search, replacement, flags=''):
    # type: (int, str, str, str, mypy.typing.Optional[str]) -> mypy.Any
    re_flags = re.MULTILINE
    if 'i' in flags:
        re_flags |= re.IGNORECASE
    if 'u' not in flags:
        replacement = evil_turn_off_python_repr_of_unicode_chars(replacement)
    regex = re.compile(string_to_search, flags=re_flags)
    replacer = Replacer.Replacer(buffer_string, regex, replacement)
    replacements_list = []  # type: list
    if 'g' in flags:
        replacements_list.extend(replacer.replace_all(start))
        replacements_list.extend(replacer.replace_all(0, end_index=start))
    else:
        replacements_list.extend(replacer.replace_all(start))
    return (replacements_list, flags)


# Parsing Input
def evil_split_on_delimiters(string):
    # type: (str) -> mypy.iterator[str]
    splitted_string = re.split(r'(?<!\\)/', string)
    # unescape escaped delimiters
    return map(lambda x: x.replace('\\/', '/'), splitted_string)


def evil_turn_off_python_repr_of_unicode_chars(replacement_string):
    # type: (str) -> str
    return re.sub(r'\\(\d+)', r'\\g<\1>', replacement_string)


def evil_parse_input(buffer_string, regex_string, point):
    # type: (str, str, int) -> mypy.Any
    args = evil_split_on_delimiters(regex_string)
    total_args = len(args[1:])
    if args[0] == '' and (total_args == 1 or total_args == 2):
        return evil_search(point, buffer_string, *args[1:])
    elif args[0] == 's' and (total_args == 2 or total_args == 3):
        return evil_substitute(point, buffer_string, *args[1:])
    else:
        return 'Format not supported!'


def main():
    # type: () -> mypy.Any
    args = sys.argv
    result = evil_parse_input(args[1], args[2], int(args[3]))
    return result


if __name__ == '__main__':
    print main()
