class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []
        added = set()

        def dfs(subset, added):
            if len(subset) == len(nums):
                output.append(subset[:])
                return
            
            for n in nums:
                if n not in added:
                    subset.append(n)
                    added.add(n)
                    dfs(subset, added)
                    subset.pop()
                    added.remove(n)
        
        dfs(subset, added)

        return output