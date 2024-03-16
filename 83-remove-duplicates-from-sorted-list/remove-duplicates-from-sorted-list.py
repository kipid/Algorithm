# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def delDup(head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None or head.next == None:
                return None
            last, curr, next = head, head, head.next
            while next != None and curr.val != next.val:
                last, curr, next = curr, next, next.next
            deleted = False
            while next != None and curr.val == next.val:
                deleted = True
                curr, next = next, next.next
            if deleted:
                last.next = curr
                return curr
            else:
                return None
        
        dummy = ListNode(-101, head)
        curr = dummy
        while (curr := delDup(curr)) != None:
            pass
        return dummy.next