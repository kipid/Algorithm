# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        last, curr, next = ListNode(next=head), head, head.next
        while count < left:
            last, curr, next = curr, next, next.next
            count += 1
        preHead = last
        while count < right:
            last, curr, next = curr, next, next.next
            curr.next = last
            count += 1
        preHead.next.next = next
        preHead.next = curr
        if left==1:
            return curr
        return head