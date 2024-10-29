# Many objects in python have built-in iterators. That's why we can conveniently iterate through an array using the key word in.
# for i in myList: ...
# For more complex objects, like Linked Lists or Binary Search Trees, we can define our own iterators.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.curr = None

    # define iterator
    def __iter__(self):
        self.curr = self.head
        return self
    
    # iterate
    def __next__(self):
        if self.curr:
            val = self.curr.val
            self.curr = self.curr.next
            return val
        else:
            raise StopIteration
        
# Initialize LinkedList
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
myList = LinkedList(head)

# Iterate through LinkedList
for n in myList:
    print(n) 

# Source: NeetCode