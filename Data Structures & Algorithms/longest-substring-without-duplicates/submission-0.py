class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        
        longest = 0
        for i in s:
            while i in window:
                window.pop(0)
            window.append(i)
            longest = max(len(window), longest)
        
        print(window)
        return longest