# Проверить деревья на равенство

# Вам даны два бинарных дерева head_1, head_2.
# Необходимо проверить, являются ли эти два дерева одинаковыми:
# имеют одинаковую структуру и одинаковые элементы на соответствующих узлах.

# Каждый узел дерева задается экземпляром класса Node, определенным ниже:

from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_go(root_r: Optional[Node], root_l: Optional[Node]) -> bool:
    if root_r is None and root_l is None:
        return True
    elif root_r is None or root_l is None:
        return False
    return (root_r.val == root_l.val
            and
            tree_go(root_r=root_r.left, root_l=root_l.left)
            and
            tree_go(root_r=root_r.right, root_l=root_l.right)
            )

def are_trees_equal(head_1: Optional[Node], head_2: Optional[Node]) -> bool:
    return tree_go(root_l=head_1, root_r=head_2)

# if __name__ == "__main__":
#     head_1 = Node(val=1, left=Node(val=2, left=None, right=None), right=Node(val=3, left=None, right=None))
#     head_2 = Node(val=1, left=Node(val=2, left=None, right=None), right=Node(val=3, left=None, right=None))
#     print(are_trees_equal(head_1=head_1, head_2=head_2))