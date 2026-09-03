class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        combination = []

        def dfs(start, summ):
            if summ > target:
                return
                
            if summ == target:
                    output.append(combination[:])
                    return

            for i in range(start, len(nums)):
                combination.append(nums[i])
                dfs(i, nums[i] + summ)
                combination.pop()

        dfs(0, 0)

        return output