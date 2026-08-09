class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_length = 0

        i = j = 0
        while j < len(s):
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            max_length = max(len(window), max_length)
            j += 1

        return max_length