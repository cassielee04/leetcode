class Solution101Recursive:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root,root)
    
    def dfs(self, root1, root2):
        
        if not root1 or not root2:
            return root1 == root2
        
        if root1 == None and root2 == None:
            return True
        
        if root1.val == root2.val:
            return self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left)

class Solution101Iterative: 
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = collections.deque([(root, root)])
        
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            
            queue.append([node1.left, node2.right])
            queue.append([node1.right, node2.left])
            
        return True
        
            
        
        