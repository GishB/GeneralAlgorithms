# TO DO: Given the root of a binary tree,
#    check whether it is a mirror of itself
#    (i.e., symmetric around its center).
#
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
# Example №1
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
# Example №2
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
def tree_go(root_r: Optional[TreeNode], root_l: Optional[TreeNode]):
    if root_r is None and root_l is None:
        return True
    elif root_r is None or root_l is None:
        return False
    return (root_r.val == root_l.val
            and
            tree_go(root_r=root_r.left, root_l=root_l.right)
            and
            tree_go(root_r=root_r.right, root_l=root_l.left)
            )

def check_tree(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    else:
        return tree_go(root_l=root.left, root_r=root.right)


if __name__ == "__main__":
    example_root = TreeNode(val=1,
                            left=TreeNode(val=2,
                                          left=None,
                                          right=TreeNode(val=3, left=None, right=None)),
                            right=TreeNode(val=2,
                                           left=TreeNode(val=3, left=None, right=None),
                                           right=TreeNode(val=3, left=None, right=None))
                            )
    print(check_tree(example_root))