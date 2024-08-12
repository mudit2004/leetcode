class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0  # A null tree is balanced and has a height of 0
            
            # Check the left subtree
            left_height = check_balance(node.left)
            if left_height == -1:
                return -1  # Not balanced
            
            # Check the right subtree
            right_height = check_balance(node.right)
            if right_height == -1:
                return -1  # Not balanced
            
            # If the current node is not balanced
            if abs(left_height - right_height) > 1:
                return -1  # Not balanced
            
            # Return the height of the subtree rooted at this node
            return max(left_height, right_height) + 1
        
        # The tree is balanced if the helper function doesn't return -1
        return check_balance(root) != -1