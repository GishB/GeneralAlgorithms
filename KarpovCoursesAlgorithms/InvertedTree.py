# Развернуть дерево

# Вам дана вершина бинарного дерева head.
# Необходимо развернуть дерево: поменять местами левого и правого потомка для каждого из потомков.

# Каждый узел дерева задается экземпляром класса Node, определенным ниже:

from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def go_invert(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return head
    head.left, head.right = go_invert(head.right), go_invert(head.left)
    return head


def invert_tree(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return head
    else:
        return go_invert(head)

# if __name__ == "__main__":
#     head_1 = Node(val=1, left=Node(val=5, left=Node(val=25), right=None),
#                          right=Node(val=9, left=Node(val=26), right=None))
#     print(invert_tree(head=head_1))