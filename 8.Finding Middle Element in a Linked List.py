'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    def findMid(self, head):
        if not head:
            return -1

        slow = fast = head
        
        # Move slow pointer one node at a time and fast pointer two nodes at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
        # return the value stored in the middle node