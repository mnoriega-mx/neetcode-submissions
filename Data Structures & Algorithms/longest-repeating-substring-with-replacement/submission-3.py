class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0

        l = r = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            if (r - l + 1 - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            r += 1
        
        return longest