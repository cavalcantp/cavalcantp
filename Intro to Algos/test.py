from typing import List, Optional
from collections import deque
# class TrieNode:
#     def __init__(self):
#         self.children ={}
#         self.isEndOfWord= False
#     def addWords(self,word):
#         curr = self
#         for c in word:
#             if c not in curr.children:
#                 curr.children[c] = TrieNode()
#             curr = curr.children[c]
#         curr.isEndOfWord=True
#     def getPrefix(self)->str: 
#         prefix = ""
#         curr= self
#         while curr and not curr.isEndOfWord: 
#             if len(curr.children)!= 1:
#                 break
#             c = next(iter(curr.children))
#             prefix+=c
#             curr=curr.children[c]
#         return prefix

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         trie= TrieNode()
#         for word in strs:
#             trie.addWords(word)
#         return trie.getPrefix()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        current1 = list1
        current2 = list2
        if current1.val <= current2.val:
            current = ListNode(val=current1.val)
            current1 = current1.next
        else:
            current = ListNode(val=current2.val)
            current2 = current2.next

        while current1 is not None or current2 is not None:
            if current1 is None:
                current.next = ListNode(val=current2.val)
                current2 = current2.next
            elif current2 is None:
                current.next = ListNode(val=current1.val)
                current1 = current1.next
            elif current1.val <= current2.val:
                current.next = ListNode(val=current1.val)
                current1 = current1.next
            else:
                current.next = ListNode(val=current2.val)
                current2 = current2.next

            
        return current

if __name__ == "__main__":
    s = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    merged = s.mergeTwoLists(list1, list2)
    print(merged)

    # # Create a deque
    # my_deque = deque()

    # # Append strings to the deque
    # my_deque.append("Hello")
    # my_deque.append("World")

    # # Pop a string from the right
    # last_item = my_deque.pop()  # "World"

    # # Pop a string from the left
    # first_item = my_deque.popleft()  # "Hello"

    # print(last_item, first_item)  # Output: World Hello

