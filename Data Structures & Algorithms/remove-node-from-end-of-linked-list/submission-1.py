# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None

        n_count = 0
        tmp = head
        while tmp != None:
            n_count += 1
            tmp = tmp.next
        target = n_count - n

        if target < 0:
            return None
        elif target == 0:
            return head.next
        
        
        tmp = head
        for i in range(target-1):
            tmp = tmp.next
        
        tmp.next = tmp.next.next

        return head
        


        