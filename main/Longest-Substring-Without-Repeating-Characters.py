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