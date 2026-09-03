class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        combination = []

        def dfs(i, summ):
            if summ == target:
                output.append(combination[:])
                return
            if i == len(nums) or summ > target:
                return
            
            combination.append(nums[i])
            dfs(i, nums[i] + summ)
            combination.pop()
            dfs(i + 1, summ)

        dfs(0, 0)

        return output