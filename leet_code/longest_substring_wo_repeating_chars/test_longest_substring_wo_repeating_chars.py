from unittest import TestCase
from longest_substring_wo_repeating_chars import length_of_longest_substring


class TestLongestSubstringWoRepeating(TestCase):
    def test_with_a_space(self):
        test_str = " "
        self.assertEqual(1, length_of_longest_substring(test_str), "test with a space")

    def test_with_the_same_char(self):
        test_str = "bbbbb"
        self.assertEqual(1, length_of_longest_substring(test_str), "test with the same char")

    def test_with_longest_string_in_the_beginning(self):
        test_str = "abcabcbb"
        self.assertEqual(3, length_of_longest_substring(test_str), "test with the string in the beginning")

    def test_with_longest_string_in_the_middle(self):
        test_str = "pwwkew"
        self.assertEqual(3, length_of_longest_substring(test_str), "test with the string in the middle")

    def test_with_longest_string_in_the_end(self):
        test_str = "dvdf"
        self.assertEqual(3, length_of_longest_substring(test_str), "test with the string in the end")







