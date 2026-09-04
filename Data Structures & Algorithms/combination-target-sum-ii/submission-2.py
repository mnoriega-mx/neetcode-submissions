class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        output = []
        combination = []

        def dfs(i, summ):
            if summ == target:
                output.append(combination[:])
                return
            if i == len(candidates) or summ > target:
                return
            
            combination.append(candidates[i])
            dfs(i + 1, candidates[i] + summ)
            combination.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, summ)

        dfs(0, 0)

        return output