class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        
        longest = 0
        for i in s:
            while i in queue:
                queue.pop(0)
            queue.append(i)
            longest = max(len(queue), longest)
        
        return longest