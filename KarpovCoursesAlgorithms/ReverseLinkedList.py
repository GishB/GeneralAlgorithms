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

#
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# def rotate_right(head: Node, k: int) -> Node:
#     if head is None or k == 0 or head.next is None:
#         out = head
#     else:
#         len_list = 0
#         while True:
#             next_value = head.next.value
#             if next_value is not None:
#                 len_list += 1
#     return out
#
#
# if __name__ == "__main__":
#     list_test = Node(1, Node(2, Node(3, Node(4, None))))
#     print(list_test.value, list_test.next.value, list_test.next.next.value, list_test.next.next.next.value)
