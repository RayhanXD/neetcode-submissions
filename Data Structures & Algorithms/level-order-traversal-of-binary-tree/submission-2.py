# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        queue = deque([root])
        levels = []

        while queue:
            nodes = len(queue)

            this_level = []

            for node in range(nodes):
                node = queue.popleft()

                this_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)

            levels.append(this_level)


        return levels

        

        
        