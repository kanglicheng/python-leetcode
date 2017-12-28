# Given the head pointer of a linked list, reverse the linked list and return the head of reversed list.
# recursive solution 
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next= None
        return new_head

# iterative solution
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next= None
        return new_head
