# 3. Longest Substring Without Repeating Characters
# Medium
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.

# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A dictionary to store the last seen position + 1 of each character in the string.
        dict_non_repeat_chars = {}
        # Marks the beginning of the current window (substring without repeats).
        start = 0
        # Keeps track of the maximum length found so far.
        result = 0

        for end in range(len(s)):
            if s[end] in dict_non_repeat_chars:
                start = max(dict_non_repeat_chars[s[end]], start)
            result = max(result, end - start + 1) 
            dict_non_repeat_chars[s[end]] = end + 1

        return result
