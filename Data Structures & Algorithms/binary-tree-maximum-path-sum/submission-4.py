# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def find_sum(root):
            if not root:
                return 0

            left_sum = max(find_sum(root.left), 0)
            right_sum = max(find_sum(root.right), 0)
            
            curr_max_sum = left_sum + root.val + right_sum
            
            self.max_sum = max(curr_max_sum, self.max_sum)

            return root.val + max(left_sum, right_sum)

        
        find_sum(root)

        return self.max_sum
