
# Задача: K-ый наименьший элемент

# Описание:
# Вам дан корень head бинарного дерева поиска (BST) и число k.
# Необходимо найти k-ый (нумерация с единицы) наименьший элемент в этом дереве поиска.

# Каждый узел дерева задается экземпляром класса Node, определенным ниже:

# Example №1: head = [3,1,4,null,2], k = 1. Ответ: 1
# Example №2: head = [5,3,6,2,4,null,null,1], k = 3. Ответ: 3

from typing import List, Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(head: Node) -> List[int]:
    stack = []
    ans = []
    curr = head
    while curr is not None or len(stack) > 0:
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        ans.append(curr.val)

        curr = curr.right
    return ans



def kth_smallest(head: Optional[Node], k: int) -> Optional[int]:
    if head is not None:
        return inorder(head=head)[k-1]
    else:
        return head


# if __name__ == "__main__":
#     example = Node(val= 5,
#                    left=Node(val=3, right=Node(val=4),
#                        left=Node(val=2,
#                                  left=Node(val=1))),
#                    right=Node(val=6))
#     print(kth_smallest(head=example, k=1))