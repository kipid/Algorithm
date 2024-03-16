# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        def firstNonDup(head: Optional[ListNode]) -> Optional[ListNode]:
            curr, next = head, head.next
            if next == None or curr.val != next.val:
                return curr
            while next != None and curr.val == next.val:
                curr, next = next, next.next
            if next == None:
                return None
            return firstNonDup(next)
        
        head = firstNonDup(head)
        if head == None:
            return None

        def delSecondDup(head: Optional[ListNode]) -> Optional[ListNode]:
            last, curr, next = head, head, head.next
            if next == None:
                return None
            while next != None and curr.val != next.val:
                last, curr, next = curr, next, next.next
            deleted = False
            while next != None and curr.val == next.val:
                deleted = True
                curr, next = next, next.next
            if deleted:
                last.next = next
                return last
            else:
                return next

        curr = head
        while (curr := delSecondDup(curr)) != None:
            pass
        return head