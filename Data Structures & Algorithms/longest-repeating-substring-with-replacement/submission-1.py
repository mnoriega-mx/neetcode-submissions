class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            
            window_len = r - l + 1
            most_frequent = max(count.values())

            replace = window_len - most_frequent

            if replace <= k:
                longest = max(window_len, longest)
                r += 1
            else:
                count[s[l]] -= 1
                l += 1
        
        return longest

