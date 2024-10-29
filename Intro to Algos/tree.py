from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def maxDepthrecursiveDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepthrecursiveDFS(root=root.left), self.maxDepthrecursiveDFS(root=root.right)) + 1

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        tree_level = deque([root])
        depth = 0
        while tree_level:
            for _ in range(len(tree_level)):
                node = tree_level.popleft()
                if node.left:
                    tree_level.append(node.left)
                if node.right:
                    tree_level.append(node.right)

            depth += 1

        return depth
    
    def maxDepthiterativeDFS(self, root: Optional[TreeNode]) -> int:
        mystack = [(root, 1)] # (node, depth)
        res = 0
        while mystack:
            node, depth = mystack.pop()
            if node: # if no node at all at tree res = 0. If reached leaf, res doesnt change
                res = max(res, depth)
                mystack.append((node.left, depth + 1))
                mystack.append((node.right, depth + 1))

        return res

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            print("Leaves")
            return True
        elif not p and q:
            return False
        elif not q and p:
            return False
        elif p.value != q.value:
            print(f"difference: {p.value}, {q.value}")
            return False
        else:
            print(f"match: {p.value}, {q.value}")
            print(f"call for left subtrees: {p.left}, {q.left}")
            left_subtree_isequal = self.isSameTree(p.left, q.left)
            print(f"call for left subtrees: {p.right}, {q.right}")
            right_subtree_is_equal = self.isSameTree(p.right, q.right)
            return left_subtree_isequal and right_subtree_is_equal

    def reverse(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        new_node = TreeNode(root.val)
        
        new_node.right = self.reverse(root.left)
        new_node.left = self.reverse(root.right)

        return new_node
    
    def equal(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q) or (p.val != q.val):
            return False

        left_eq = self.equal(p.left, q.left)
        right_eq = self.equal(p.right, q.right)

        return left_eq and right_eq

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # DFS recursive - O(n) time, O(h) space
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (
                (left.val == right.val) 
                and dfs(left.left, right.right) 
                and dfs(left.right, right.left)
                )

        #return dfs(root.left, root.right)

        # DFS iteratively - O(n) time, O(h) space
        #if not root:
        #    return True
        #stack = [(root.left, root.right)]
        #while stack:
        #    left, right = stack.pop()
        #    if not left and not right:
        #        continue
        #    if not left or not right:
        #        return False
        #    if left.val != right.val:
        #        return False
        #    
        #    stack.append((left.left, right.right))
        #    stack.append((left.right, right.left))

        #return True



        # BFS - O(n) time, O(h) space
        if not root:
            return True
        q = deque([(root.left, root.right)])
        while q:
            left, right = q.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            q.append((left.left, right.right))
            q.append((left.right, right.left))

        return True
            


        # DFS recursive approach
        #reversed_root = self.reverse(root)
        #return self.equal(root, reversed_root)


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Recursive DFS - O(n) time, O(h) space
        def dfs(root, sub_sum):
            if not root:
                return False
            if not root.left and not root.right:
                return (sub_sum - root.val) == 0
            if not root.left:
                return dfs(root.right, sub_sum - root.val)
            if not root.right:
                return dfs(root.left, sub_sum - root.val)

            return dfs(root.left, sub_sum - root.val) or dfs(root.right, sub_sum - root.val)

        #return dfs(root, targetSum)


        # Iterative DFS - O(n) time, O(h) space
        def dfs_iterative(root, targetSum):
            if not root:
                return False

            stack = [(root, targetSum)]
            while stack:
                node, subsum = stack.pop()
                if not node.left and not node.right and subsum - node.val == 0:
                    return True
                if node.right:
                    stack.append((node.right, subsum - node.val))
                if node.left:
                    stack.append((node.left, subsum - node.val))

            return False

        #return dfs_iterative(root, targetSum)

        # BFS - O(n) time, O(w) max width space, w = O(n) full binary tree
        def bfs(root, targetSum):
            if not root:
                return False

            level_q = deque([(root, targetSum)])

            while level_q:
                node, subsum = level_q.popleft()
                if not node.left and not node.right and node.val - subsum == 0:
                    return True
                if node.left:
                    level_q.append((node.left, subsum - node.val))
                if node.right:
                    level_q.append((node.right, subsum - node.val))

            return False

        return bfs(root, targetSum)

    def test(self, current):
        while current.left:
            current = current.left

        return current
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root): # O(n) time
            if not root:
                return 0
            nodes = 0
            q = deque([root])
            while q:
                node = q.pop()
                if node:
                    nodes += 1
                    q.append(node.left)
                    q.append(node.right)

            return nodes
        # return dfs(root)

        # O(log(n)*log(n)) time ->
        def always_left(root):
            if not root:
                return 0
            current = root
            level = 1
            while current.left:
                level += 1
                current = current.left

            return level

        def always_right(root):
            if not root:
                return 0
            current = root
            level = 1
            while current.right:
                level += 1
                current = current.right

            return level

        def recursive_bs(root):
            if not root:
                return 0
            l, r = always_left(root), always_right(root)
            if l == r:
                return (2 ** l) - 1
                
            left_nodes = recursive_bs(root.left)
            right_nodes = recursive_bs(root.right)

            return 1 + left_nodes + right_nodes

        #return recursive_bs(root)

        def iterative_bs(root):
            nodes = 0
            q = deque([root])
            while q:
                node = q.pop()
                if node:
                    l, r = always_left(node), always_right(node)
                    if l == r:
                        nodes += 2 ** l - 1
                    else:
                        nodes += 1
                        q.append(node.left)
                        q.append(node.right)

            return nodes

        # return iterative_bs(root)

        def bfs_inspired(root):
            nodes = 0
            q = deque([root])
            level = 0
            while q:
                node = q.popleft()
                if node:
                    l, r = always_left(node), always_right(node)
                    if l == r:
                        nodes += 2 ** l - 1
                    else:
                        nodes += 1
                        q.append(node.left)
                        q.append(node.right)
            
            return nodes
        
        return bfs_inspired(root)


    

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(value=3)
    root.left = TreeNode(value=9)
    root.right = TreeNode(value=20)
    root.right.left = TreeNode(value=15)
    root.right.right = TreeNode(value=7)
    root.right.right.right = TreeNode(value=2)
    root.right.right.right.left = TreeNode(value=1)

    depth = s.maxDepthrecursiveDFS(root=root)
    #print(f"tree depth is {depth}")
    bfs = s.maxDepthBFS(root=root)
    #print(f"tree depth with BFS algo is {bfs}")
    iterative_dfs = s.maxDepthiterativeDFS(root=root)
    #print(f"tree depth with iter DFS algo is {iterative_dfs}")
    p = TreeNode(value=1)
    q = TreeNode(value=1)
    p.left = TreeNode(value=2)
    q.right = TreeNode(value=2)
    print(s.isSameTree(p, q))

    current = s.test(root)
    print("test")
    print(f"root is {root.value} and current is {current.value}")

    tree = TreeNode(value=1)
    tree.left = TreeNode(value=2)
    tree.right = TreeNode(value=3)
    tree.left.left = TreeNode(value=4)
    tree.left.right = TreeNode(value=5)
    tree.right.left = TreeNode(value=6)

    nodes = s.countNodes(tree)
    print(nodes)
        

