# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2:
            return None
        out = ListNode(0)
        if list1.val < list2.val:
            out.val = list1.val
            list1 = list1.next
        else:
            out.val = list2.val
            list2 = list2.next
        
        tmp = out
        # loop while both of our lists are not none
        while list1 or list2:
            
            # if one list is none, append the rest of the other to the output
            if list1 == None:
                tmp.next = list2
                break
            elif list2 == None:
                tmp.next = list1
                break
            
            if list1.val < list2.val:
                tmp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tmp.next = ListNode(list2.val)
                list2 = list2.next
            tmp = tmp.next
        return out
