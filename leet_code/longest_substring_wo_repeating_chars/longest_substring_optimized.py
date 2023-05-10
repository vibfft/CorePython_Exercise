# const lengthOfLongestSubstring = function(s) {
#     if(s.length <= 1) return s.length;
    
#     const seen = {};
#     let left = 0, longest = 0;
    
#     for(let right = 0; right < s.length; right++) {
#         const currentChar = s[right];
#         const previouslySeenChar = seen[currentChar];
        
#         if(previouslySeenChar >= left) {
#           left = previouslySeenChar + 1;
#         }
        
#         seen[currentChar] = right;
        
#         longest = Math.max(longest, right - left + 1);
#     }
    
#     return longest;
# };

def longest_string(s):

    seen_chars = {}
    left = 0
    longest = 0

    for right in range(len(s)):
        curr_char = s[right]
        if curr_char not in seen_chars:
            seen_chars[curr_char] = right
            prev_seen_char = right

        if prev_seen_char >= left:
            left = prev_seen_char + 1

        seen_chars[curr_char] = right

        longest = max(longest, right - left + 1)

    return longest

def main():
    for s in ["dvdf"]:
        # for s in ["dvdf", "bbbbb", "abcabcbb", "pwwkew"]:
        print(longest_string(s))

