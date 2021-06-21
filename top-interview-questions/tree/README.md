# Tree

## Problem Solutions

### Problem 104: Maximum Depth of Binary Tree
[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#### Approach 1 
##### Recursive DFS

1) Recursion 사용해서 root 값이 없을때 함수를 나올수있도록 if 문을 만들어준다
2) 왼쪽의 leaf node 까지 돈다, 돌때마다 1을 더해준다
3) 오른쪽 leaf node 까지 돈다, 돌때마다 1 을 더해준다 
4) 왼쪽 오른쪽 중의 max 값으로 리턴하도록 한다. 

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        
        return max(left,right)
```
Runtime: O(N)
Space Complexity: O(N)

#### Approach 2 
##### Iterative DFS

1) Node 값들을 넣어줄 stack을 만든다
2) 처음 노드값과 depth = 0 을 stack 에 넣어준다
3) while 문에 stack 이 비어있지 않을때 root과 depth 값을 pop 해준다
4) depth 는 현재 depth 와 pop한 depth 중에 max 값으로 지정해준다
4) root.left 가 존재할때 stack 에 root.left 와 depth + 1 을 넣어준다
5) root. right 이 존재한다면 stack 에 root.right 과 depth + 1 을 넣어준다
6) 리턴 depth 를 해준다. 

``` python
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
```
Runtime: O(N)
Space Complexity: O(N)

### Problem 101: Symmetric Tree
[Maximum Depth of Binary Tree](https://leetcode.com/problems/symmetric-tree/)
Given the root of a binary tree, check whether it is a mirror of itself 

#### Approach 1 
##### Recursive DFS
1) Helper Function 을 만들어준다. 
2) helper funrction 에 root1, root2 를 넣어주며 비교한다
3) 두 노드 가 Null 값이라면 true 로 반환
4) 두 노드중 하나만 있으면 False 값으로 반환
5) 두 노드값이 같다면, root1.left == root2.right, root1.right == root2.left 값이 같은지 recursively 비교 한다

```python 
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root,root)
    
    def dfs(self, root1, root2):
        
        if not root1 or not root2:
            return root1 == root2
        
        if root1 == None and root2 == None:
            return True
        
        if root1.val == root2.val:
            return self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left)
```
Runtime: O(N)
Space Complexity: O(N)

#### Approach 2
##### Iterative BFS
1) 큐에 노드 2개를 넣는다
2) 큐가 비어있지 않을때 root1 , root를 팝해준다
3) 둘다 null 값이면 true 이므로 계속 돌린다
4) 둘값이 다르다면 false 를 반환한다
5) 둘중에 하나만 있다면 false 를 반환한다
6) 둘값이 같다면 큐에 서로 대칭되는 노드를 넣어준다

```python 
class Solution:
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
```

Runtime: O(N)
Space Complexity: O(N)

### Problem 94: Binary Tree Inorder Traversal
[Maximum Depth of Binary Tree](https://leetcode.com/problems/binary-tree-inorder-traversal/)
Given the root of a binary tree, return the inorder traversal of its nodes' values.

In-Order: left -> root -> right
Pre-Order: root -> left -> right
Post-Order: left -> right -> root

#### Approach 1 
##### Recursive DFS

1) root 이 없다면 None 으로 반환
2) if root.left 라면 함수를 재귀로 root.left 넣어서 돌린다
3) root value 를 res 리스트에 넣어준다
4) if root.right 라면 함수를 재귀로 root.right 넣어서 돌린다
5) res list 반환

```python 
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
```
Runtime: O(N)
Space Complexity: O(N)

#### Approach 2
##### Iterative DFS
1) stack 과 res 를 initialize 해준다
2) root 이 있거나 stack 이 안비었다면 계속 돌린다
3) root 이있다면 stack 에 root 을 넣어줌, root = roo.left
4) 더이상 root 이 없다면 stack 에서 root 값을 pop 한다. 
5) res 에 root 발류를 넣어줌
5) root = root.right
6) res 반환

```python
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
```