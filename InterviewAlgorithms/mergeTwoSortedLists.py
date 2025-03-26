from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2




if __name__ == "__main__":
    list1 = ListNode(4, ListNode(5, ListNode(6)))
    list2 = ListNode(1, ListNode(2, ListNode(3)))
    test = mergeTwoLists(list1, list2)
    print("stop")