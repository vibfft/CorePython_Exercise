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
def length_of_longest_substring(s: str) -> int:
    str_accumulator = ""
    str_max = ""
    for i, c in enumerate(s):
        if c not in str_accumulator:
            str_accumulator += c
        else:
            str_accumulator = str_accumulator[str_accumulator.find(c) + 1:] + c
            # print(f"inside str_acc: {str_accumulator}, str_max: {str_max}, char: {c}")
        str_max = str_accumulator if len(str_accumulator) > len(str_max) else str_max
        # print(f"str_acc: {str_accumulator}, str_max: {str_max}, char: {c}")
    if len(str_max) == 0:
        str_max = str_accumulator
    return len(str_max)


def main():
    # for s in ["dvdf", "nfpdmpi"]:
    for s in ["dvdf"]:
        print(length_of_longest_substring(s))


if __name__ == '__main__':
    main()
