from unittest import TestCase
from longest_palindromic_substring import longest_palindrome

class TestLongestPalindrome(TestCase):
    def test_palindrome_in_the_beginning(self):
        input_str = "babad"
        self.assertEqual("bab", longest_palindrome(input_str))
