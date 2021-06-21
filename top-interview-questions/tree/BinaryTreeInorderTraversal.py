class Solution94Iterative:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        
        return res
class Solution94Recursive:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, root, res):
        if root != None:
            if root.left:
                self.dfs(root.left, res)

            res.append(root.val)

            if root.right:
                self.dfs(root.right,res)
        
        