class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest_sequence = 0
        for num in nums:
            if num-1 in nums_set:
                continue
            print(num)
            current_sequence = 1
            start = num
            while start+1 in nums_set:
                print(start)
                current_sequence += 1
                start = start+1
            longest_sequence = max(current_sequence, longest_sequence)
            
        return longest_sequence