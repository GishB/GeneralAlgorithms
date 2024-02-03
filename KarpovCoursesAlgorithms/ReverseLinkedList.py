"""
Task № 4.

Yoy have one direction sequence. You need to rotate its values by k position.

Your task is to write function rotate_right(head, k) which return expected list.

Limitations:
    1. You have to work with one list. You can`t create a new one!
    2. You have to switch connections inside the list.
    3. Class Node will represent the one direction sequence object.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

For example:
    1.
        head = [1, 2, 3, 4, 5]
        k = 2
        return [4, 5, 1, 2, 3, ]
"""
from typing import Optional


def rotate_right(one_directional_list: Optional[object], k: Optional[int]) -> Optional[object]:
    if one_directional_list is None or k == 0 or one_directional_list.next is None:
        pass
    else:
        len_list = 1
        p = one_directional_list
        while p.next is not None:
            p = p.next
            len_list += 1
        k %= len_list
        p.next = one_directional_list
        for i in range(len_list - k):
            p = p.next
        one_directional_list = p.next
        p.next = None
    return one_directional_list


if __name__ == "__main__":
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next


    list_test = Node(1, Node(2, Node(3, Node(4, None))))
    # print(list_test.value, list_test.next.value, list_test.next.next.value, list_test.next.next.next.value)
    rotate_right(list_test, 2)
