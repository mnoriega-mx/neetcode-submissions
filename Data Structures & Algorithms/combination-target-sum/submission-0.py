class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        combination = []

        def dfs(start):
            summ = sum(combination)

            if summ > target:
                return
                
            if sum(combination) == target:
                    output.append(combination[:])
                    return

            for i in range(start, len(nums)):
                combination.append(nums[i])
                dfs(i)
                combination.pop()

        dfs(0)

        return output