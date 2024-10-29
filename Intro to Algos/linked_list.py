from typing import Optional, List

def print_ll(head):
    while head:
        print(f"{head.val} ->")
        head = head.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_ll(self, head):
        while head:
            print(f"{head.val} ->")
            head = head.next
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(val=-1)
        merged = head
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            print(f"Comparing {curr1.val} and {curr2.val}")
            if curr1.val <= curr2.val:
                print(f"Add {curr1.val}")
                merged.next = curr1
                curr1 = curr1.next
            else:
                print(f"Add {curr2.val}")
                merged.next = curr2
                curr2 = curr2.next
            merged = merged.next
            self.print_ll(curr1)
            print("----")
            self.print_ll(curr2)

        if curr1:
            merged.next = curr1
        else:
            merged.next = curr2
        
        return head.next

    def mergeSortedLLs_clean(self, list1, list2):
        # clean solution
        dummy = ListNode()
        node = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next

if __name__ == "__main__":
    head = ListNode(val=1)
    curr = head
    for i in range(2, 6):
        curr.next = ListNode(val=i)
        curr = curr.next

    head2 = ListNode(val=2)
    curr = head2
    for i in range(2, 8, 2):
        curr.next = ListNode(val=i)
        curr = curr.next

    print("list 1:")
    print_ll(head)
    print("list 2:")
    print_ll(head2)

    merged = Solution().mergeTwoLists(head, head2)
    print("merged")
    print_ll(merged)

    