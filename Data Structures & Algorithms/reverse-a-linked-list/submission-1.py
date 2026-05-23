# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        
        nxt = head.next
        tmp = nxt.next
        head.next = None
        while nxt is not None:
            nxt.next = head
            head = nxt
            nxt = tmp
            if nxt is not None:
                tmp = nxt.next
        return head
