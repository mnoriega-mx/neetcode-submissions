class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            tgt = target - nums[i]
            if tgt in visited:
                return [visited[tgt], i]
            visited[nums[i]] = i
            