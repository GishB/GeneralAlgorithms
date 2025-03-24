# Task name: Поворот односвязного списка
# Desc general: Вам дана голова односвязного списка head.
# Вам необходимо «повернуть» его направо на k позиций.


# Example: 1 - 2 - 3 - 4 - 5
# Example solution: 4 - 5 - 1 - 2 - 3

# Task description:
# Напишите функцию rotate_right(head, k),
# которая будет возвращать голову повернутого листа.
# Вам нельзя создавать новый односвязный список — нужно все изменения делать с существующим
# (т.е. переставлять связи внутри него).

# Считайте, что односвязный список задан классом Node
# (при этом head есть экземпляр данного класса), код которого дан ниже.

from typing import Optional, Tuple


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

def rotate_right(head, k):
    if not head or k <= 0:
        return head

    # Step 1: Find the length of the linked list
    length = 1
    tail = head
    while tail.next:
        length += 1
        tail = tail.next

    # Step 2: Find the new tail (node before the new head)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    # Step 3: Detach and move the last k nodes to front
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head


# if __name__ == "__main__":
#     example = Node(1, Node(2, Node(3, Node(4, Node(5)))))
#     solution = Node(5, Node(4, Node(1, Node(2, Node(3)))))
#     tmp = rotate_right(example, 1)
#     print("stop")