import re
import sys

sys.path.insert(0, '../../')
from lib import Replacer
from test import Tester


class ReplaceOnceTester(Tester.Tester):

    def __init__(self):
        super(ReplaceOnceTester, self).__init__(ReplaceOnceTester)

    def test_standard_case_no_repeat(self):
        r = Replacer.Replacer('hello', re.compile('he', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(0)
        assert test_result1 == ['he', 'bye', '0'], (
            'Expected: ["he", "bye", "0"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

    def test_standard_case_with_repeat(self):
        r = Replacer.Replacer('hellohe', re.compile('he', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(0)
        assert test_result1 == ['he', 'bye', '0'], (
            'Expected: ["he", "bye", "0"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == ['he', 'bye', '5'], (
            'Expected: ["he", "bye", "5"], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5)
        assert test_result3 == ['he', 'bye', '5'], (
            'Expected: ["he", "bye", "5"], got: {}'.format(test_result3))

        test_result4 = r.replace_once(6)
        assert test_result4 == [], (
            'Expected: [], got: {}'.format(test_result4))

    def test_start_index_too_small_no_match(self):
        r = Replacer.Replacer('hellohe', re.compile('i', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(-1)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

    def test_start_index_too_small_has_match_anywhere(self):
        r = Replacer.Replacer('hllohe', re.compile('he', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(-1)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

    def test_start_index_too_small_has_match_at_start(self):
        r = Replacer.Replacer('iello', re.compile('i', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(-1)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

    def test_start_index_too_small_has_match_at_end(self):
        r = Replacer.Replacer('helloi', re.compile('i', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(-1)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

    def test_start_index_too_big_no_match(self):
        r = Replacer.Replacer('helloi', re.compile('j', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(6)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

    def test_start_index_too_big_match_at_start(self):
        r = Replacer.Replacer('hello', re.compile('he', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(6)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

    def test_start_index_too_big_match_at_middle(self):
        r = Replacer.Replacer('helloi', re.compile('i', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(6)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

    def test_end_index_too_small_no_match(self):
        r = Replacer.Replacer('helloi', re.compile('j', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(0, -1)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3, -1)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5, -1)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

        test_result4 = r.replace_once(-1, -1)
        assert test_result4 == [], (
            'Expected: [], got: {}'.format(test_result4))

        test_result5 = r.replace_once(6, -1)
        assert test_result5 == [], (
            'Expected: [], got: {}'.format(test_result5))

    def test_end_index_too_small_match_at_start(self):
        r = Replacer.Replacer('helloi', re.compile('he', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(0, -1)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3, -1)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5, -1)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

        test_result4 = r.replace_once(-1, -1)
        assert test_result4 == [], (
            'Expected: [], got: {}'.format(test_result4))

        test_result5 = r.replace_once(6, -1)
        assert test_result5 == [], (
            'Expected: [], got: {}'.format(test_result5))

    def test_end_index_too_small_match_at_middle(self):
        r = Replacer.Replacer('helloi', re.compile('i', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(0, -1)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3, -1)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5, -1)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

        test_result4 = r.replace_once(-1, -1)
        assert test_result4 == [], (
            'Expected: [], got: {}'.format(test_result4))

        test_result5 = r.replace_once(6, -1)
        assert test_result5 == [], (
            'Expected: [], got: {}'.format(test_result5))

    # FIXME: need to test when there is no match, match at beginning only, and match second char+
    def test_end_index_smaller_than_start_no_match(self):
        r = Replacer.Replacer('helloi', re.compile('j', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(1, 0)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3, 0)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5, 0)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

        test_result4 = r.replace_once(6, 0)
        assert test_result4 == [], (
            'Expected: [], got: {}'.format(test_result4))

        test_result5 = r.replace_once(5, 3)
        assert test_result5 == [], (
            'Expected: [], got: {}'.format(test_result5))

        test_result6 = r.replace_once(6, 3)
        assert test_result6 == [], (
            'Expected: [], got: {}'.format(test_result6))

        test_result7 = r.replace_once(6, 5)
        assert test_result7 == [], (
            'Expected: [], got: {}'.format(test_result7))

        test_result8 = r.replace_once(10, 6)
        assert test_result8 == [], (
            'Expected: [], got: {}'.format(test_result8))

    def test_end_index_smaller_than_start_match_at_start(self):
        r = Replacer.Replacer('helloi', re.compile('he', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(1, 0)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3, 0)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5, 0)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

        test_result4 = r.replace_once(6, 0)
        assert test_result4 == [], (
            'Expected: [], got: {}'.format(test_result4))

        test_result5 = r.replace_once(5, 3)
        assert test_result5 == [], (
            'Expected: [], got: {}'.format(test_result5))

        test_result6 = r.replace_once(6, 3)
        assert test_result6 == [], (
            'Expected: [], got: {}'.format(test_result6))

        test_result7 = r.replace_once(6, 5)
        assert test_result7 == [], (
            'Expected: [], got: {}'.format(test_result7))

        test_result8 = r.replace_once(10, 6)
        assert test_result8 == [], (
            'Expected: [], got: {}'.format(test_result8))

    def test_end_index_smaller_than_start_match_at_middle(self):
        r = Replacer.Replacer('helloi', re.compile('ll', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(1, 0)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3, 0)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5, 0)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

        test_result4 = r.replace_once(6, 0)
        assert test_result4 == [], (
            'Expected: [], got: {}'.format(test_result4))

        test_result5 = r.replace_once(5, 3)
        assert test_result5 == [], (
            'Expected: [], got: {}'.format(test_result5))

        test_result6 = r.replace_once(6, 3)
        assert test_result6 == [], (
            'Expected: [], got: {}'.format(test_result6))

        test_result7 = r.replace_once(6, 5)
        assert test_result7 == [], (
            'Expected: [], got: {}'.format(test_result7))

        test_result8 = r.replace_once(10, 6)
        assert test_result8 == [], (
            'Expected: [], got: {}'.format(test_result8))

    def test_end_index_too_big_no_match(self):
        r = Replacer.Replacer('helloi', re.compile('j', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(0, 6)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3, 6)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5, 6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_end_index_too_big_match_at_start(self):
        r = Replacer.Replacer('helloi', re.compile('he', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(0, 6)
        assert test_result1 == ['he', 'bye', '0'], (
            'Expected: ["he", "bye", "0"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3, 6)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5, 6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_end_index_too_big_match_at_middle(self):
        r = Replacer.Replacer('helloi', re.compile('ll', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(0, 6)
        assert test_result1 == ['ll', 'bye', '2'], (
            'Expected: ["ll", "bye", "2"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3, 6)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(5, 6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_regex_not_exist(self):
        r = Replacer.Replacer('helloi', re.compile('bye', flags=re.MULTILINE), 'hi')

        test_result1 = r.replace_once(0)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_regex_is_empty(self):
        r = Replacer.Replacer('helloi', re.compile(''), 'hi')

        test_result1 = r.replace_once(0)
        assert test_result1 == ['', 'hi', '0'], (
            'Expected: ["", "hi", "0"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == ['', 'hi', '3'], (
            'Expected: ["", "hi", "3"], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == ['', 'hi', '6'], (
            'Expected: ["", "hi", "6"], got: {}'.format(test_result3))

    def test_regex_produces_empty_matches(self):
        r = Replacer.Replacer('helloi', re.compile('^'), 'hi')

        test_result1 = r.replace_once(0)
        assert test_result1 == ['', 'hi', '0'], (
            'Expected: ["", "hi", "0"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_regex_is_superset_no_match(self):
        r = Replacer.Replacer('helloi', re.compile('j', flags=re.MULTILINE), '')

        test_result1 = r.replace_once(0)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_regex_is_superset_at_start(self):
        r = Replacer.Replacer('helloi', re.compile('helloworld', flags=re.MULTILINE), 'hello')

        test_result1 = r.replace_once(0)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_regex_is_superset_at_middle(self):
        r = Replacer.Replacer('helloi', re.compile('lloworld', flags=re.MULTILINE), 'hello')

        test_result1 = r.replace_once(0)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_replacement_is_empty_no_match(self):
        r = Replacer.Replacer('helloi', re.compile('j', flags=re.MULTILINE), '')

        test_result1 = r.replace_once(0)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_replacement_is_empty_match_at_start(self):
        r = Replacer.Replacer('helloi', re.compile('hello', flags=re.MULTILINE), '')

        test_result1 = r.replace_once(0)
        assert test_result1 == ['hello', '', '0'], (
            'Expected: ["hello", "", "0"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_replacement_is_empty_match_at_middle(self):
        r = Replacer.Replacer('helloi', re.compile('ll', flags=re.MULTILINE), '')

        test_result1 = r.replace_once(0)
        assert test_result1 == ['ll', '', '2'], (
            'Expected: ["ll", "", "2"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_replacement_has_back_references_no_match(self):
        r = Replacer.Replacer('helloi', re.compile('bye', flags=re.MULTILINE), '\\g<0>')

        test_result1 = r.replace_once(0)
        assert test_result1 == [], (
            'Expected: [], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_replacement_has_back_references_match_at_start(self):
        r = Replacer.Replacer('helloi', re.compile('hello', flags=re.MULTILINE), '\\g<0>')

        test_result1 = r.replace_once(0)
        assert test_result1 == ['hello', 'hello', '0'], (
            'Expected: ["hello", "hello", "0"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == [], (
            'Expected: [], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_replacement_has_back_references_match_at_middle(self):
        r = Replacer.Replacer('helloi', re.compile('lo', flags=re.MULTILINE), '\\g<0>')

        test_result1 = r.replace_once(0)
        assert test_result1 == ['lo', 'lo', '3'], (
            'Expected: ["lo", "lo", "3"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(3)
        assert test_result2 == ['lo', 'lo', '3'], (
            'Expected: ["lo", "lo", "3"], got: {}'.format(test_result2))

        test_result3 = r.replace_once(6)
        assert test_result3 == [], (
            'Expected: [], got: {}'.format(test_result3))

    def test_replacement_in_middle_with_beginning_of_line_regex(self):
        r = Replacer.Replacer('hello\nworld\nbye', re.compile('^world', flags=re.MULTILINE), 'bye')

        test_result1 = r.replace_once(0)
        assert test_result1 == ['world', 'bye', '6'], (
            'Expected: ["world", "bye", "6"], got: {}'.format(test_result1))

        test_result2 = r.replace_once(6)
        assert test_result2 == ['world', 'bye', '6'], (
            'Expected: ["world", "bye", "6"], got: {}'.format(test_result2))
