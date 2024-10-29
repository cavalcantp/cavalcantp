from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 530 - Minimum absolute difference in BST
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.previous_value = None
        # Recursive approach
        def in_order_traversal(root):
            if not root:
                return

            in_order_traversal(root.left)

            if self.previous_value is not None:
                self.min_diff = min(self.min_diff, abs(root.val - self.previous_value))
            
            self.previous_value = root.val

            in_order_traversal(root.right)

        #in_order_traversal(root)
        #return self.min_diff

        # DFS iterative
        def dfs_iterative(root):
            min_diff = float('inf')
            prev_value = None
            stack = []
            current = root

            while stack or current:
                # Go to the leftmost node
                while current:
                    stack.append(current)
                    current = current.left
                
                # Process the node
                current = stack.pop()
                if prev_value is not None:
                    min_diff = min(min_diff, current.val - prev_value)
                prev_value = current.val
                
                # Move to the right subtree
                current = current.right
            
            return min_diff

        # return dfs_iterative(root)

        def inorderTraversal(root):
            res = []
            if root:
                node = inorderTraversal(root.left)
                res.append(root.val)
                res += inorderTraversal(root.right)

            return res

        def findMinDiff(arr, n):
            mindiff = float("inf")
            for i in range(1, n):
                mindiff = min(mindiff, abs(arr[i] - arr[i-1]))

            return mindiff

        traversal_order = inorderTraversal(root)
        return findMinDiff(traversal_order, len(traversal_order))

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Recursive approach - O(n) time, as it goes through all elements, O(h) space
        def build_subtree(subnums):
            if not subnums:
                return
            root_index = len(subnums) // 2
            root = TreeNode(subnums[root_index])

            root.left = build_subtree(subnums[:root_index])
            root.right = build_subtree(subnums[root_index+1:])

            return root

        # return build_subtree(nums)

        # Recursive approach, but indices based - even though O(h) recursion depth, space is minimized because storying scalars instead of arrays
        def build_subtree_indices(l, r):
            if r < l:
                return 
            root_index = (r + l)//2
            root = TreeNode(nums[root_index])
            root.left = build_subtree_indices(l, root_index - 1)
            root.right = build_subtree_indices(root_index+1, r)

            return root
        #  return build_subtree_indices(0, len(nums) - 1)

        def iterative(nums):
            if not nums:
                return
            l, r = 0, len(nums) - 1
            root = TreeNode(val=nums[(l + r)//2])
            stack = [(root, l, r)]
            while stack:
                node, l, r = stack.pop()
                mid = (l + r) // 2

                if l < mid:
                    print(l)
                    node.left = TreeNode(val=nums[(l + mid - 1) // 2])
                    stack.append((node.left, l, mid - 1))

                if r > mid:
                    print(r)
                    node.right = TreeNode(val=nums[(mid + 1 + r) // 2])
                    stack.append((node.right, mid + 1, r))

            return root
        return iterative(nums)

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(val=5)
    root.left = TreeNode(val=1)
    root.right = TreeNode(val=10)
    root.right.left = TreeNode(val=6)
    root.right.right = TreeNode(val=11)
    root.right.right.right = TreeNode(val=13)
    root.right.right.right.left = TreeNode(val=12)

    s = Solution()
    print(s.getMinimumDifference(root))

    bst = s.sortedArrayToBST([0,1,2,3,4,5,6,7])
    print("check")
