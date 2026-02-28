# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traversal(root, ans):
            if not root:
                return

            traversal(root.left, ans)
            traversal(root.right, ans)
            ans.append(root.val)
            
        traversal(root, ans)
        return ans