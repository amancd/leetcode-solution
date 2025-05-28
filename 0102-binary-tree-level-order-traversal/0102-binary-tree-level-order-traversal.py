# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Initialize the queue with the root
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()  # Dequeue the front node
                level_values.append(node.val)  # Record the value
                
                # Enqueue the children of the current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_values)  # Add the current level's values to the result
        
        return result
        