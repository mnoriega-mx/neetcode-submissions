class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()

        for i in nums:
            hashSet.add(i)
        
        longest = 0
        for i in nums:
            if i-1 in hashSet:
                continue
            
            length = 0
            while i in hashSet:
                length += 1
                i += 1
            
            longest = max(length, longest)
        
        return longest