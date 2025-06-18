# https://leetcode.com/problems/range-sum-of-bst/description/

# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    def inordered(root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.val < low:
            return inordered(root.right)
        elif root.val > high:
            return inordered(root.left)
        else:
            return root.val + inordered(root.left) + inordered(root.right)
    return inordered(root)

if __name__ == "__main__":
    test = rangeSumBST(
        TreeNode(10,
                 left=TreeNode(5, TreeNode(3), TreeNode(7)),
                 right=TreeNode(15, right=TreeNode(18))), 7, 15)
    print(test)
