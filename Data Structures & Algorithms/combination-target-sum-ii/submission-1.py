class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        output = []
        combination = []

        def dfs(start, summ):
            if summ == target:
                output.append(combination[:])
                return
            if start > len(candidates) or summ > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                combination.append(candidates[i])
                dfs(i + 1, summ + candidates[i])
                combination.pop()
                prev = candidates[i]
            
        dfs(0, 0)
    
        return output