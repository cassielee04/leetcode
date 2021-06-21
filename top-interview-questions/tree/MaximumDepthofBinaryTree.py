class Solution104Recursive:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        
        return max(left,right)

class Solution104Iterative:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        visited = []
        depth = 0
        
        if root is None:
            return 0
        
        stack.append((root, depth+1))
        while stack:
            root, cur_depth = stack.pop()
            depth = max(cur_depth, depth)            
            if root.left:
                stack.append((root.left, cur_depth + 1))

            if root.right:
                stack.append((root.right, cur_depth + 1))
        
        return depth
                
    
    