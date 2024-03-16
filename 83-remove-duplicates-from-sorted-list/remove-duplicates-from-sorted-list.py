# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last, curr = dummy, head
        while curr != None and (next := curr.next) != None:
            while next != None and curr.val != next.val:
                last, curr, next = curr, next, next.next
            deleted = False
            while next != None and curr.val == next.val:
                deleted = True
                curr, next = next, next.next
            if deleted:
                last.next = curr
                if curr == None:
                    break
                last, curr = curr, curr.next
            else:
                break
        return dummy.next