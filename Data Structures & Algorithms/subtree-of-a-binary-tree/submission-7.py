# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subRoot):
            if root == None:
                return False
            elif root.val == subRoot.val:
                return compareDFS(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)
            else:
                return dfs(root.left, subRoot) or dfs(root.right, subRoot)
                

        def compareDFS(root, subRoot):
            if root == None and subRoot == None:
                return True
            elif root == None or subRoot == None:
                return False
            elif root.val == subRoot.val:
                return compareDFS(root.left, subRoot.left) and compareDFS(root.right, subRoot.right)
            else:
                return False

        return dfs(root, subRoot)