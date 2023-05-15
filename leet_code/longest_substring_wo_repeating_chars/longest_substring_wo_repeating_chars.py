# Given a string s, find the length of the longest
# substring
#  without repeating characters.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#

# first look for any repeat char
import sys


def length_of_longest_substring(s: str) -> int:

    # a b c b d c a
    longest = 0
    seen_chars = []
    left = 0  # base pointer, only increments when a repeat char is encountered
    right = 0 # traverses the string till a repeat char is encountered

    index = 0  # this is for debugging
    while left < len(s) - 1:
        index += 1
        # if index == 10:
            # sys.exit(1)

        # print(f"s {s[left]}, index: {left}, seen_char: {seen_chars}, longest: {longest}")
        if s[right] not in seen_chars:
            seen_chars.append(s[right])
            if len(seen_chars) > longest:
                longest = len(seen_chars)
            if right < len(s) - 1: # dvdf, f is at index 'len(s) - 1', right can't be equal to 'len(s) - 1'
                right += 1
                # print(f"right index {right}")
        else:
            left += 1
            seen_chars = []
            seen_chars.append(s[left])
            right = left + 1 # increment right index from the new left index base
            # print(f"after match => s {s[left]}, index: {left}, seen_char: {seen_chars}, longest: {longest}")
    return longest


def main():
    for s in ["dvdf"]:
        # for s in ["dvdf", "bbbbb", "abcabcbb", "pwwkew"]:
        print(length_of_longest_substring(s))


if __name__ == '__main__':
    main()
