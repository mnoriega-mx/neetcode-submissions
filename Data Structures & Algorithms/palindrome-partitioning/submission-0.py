class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        partition = []

        def isPalindrome(partition):
            if not partition:
                return False
            i, j = 0, len(partition) - 1
            while i < j:
                if partition[i] != partition[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def dfs(i, j):
            if j == len(s):
                if i == j:
                    output.append(partition[:])
                return
            
            if isPalindrome(s[i : j + 1]):
                partition.append(s[i : j + 1])
                dfs(j + 1, j + 1)
                partition.pop()
            
            dfs(i, j + 1)
        
        dfs(0, 0)

        return output