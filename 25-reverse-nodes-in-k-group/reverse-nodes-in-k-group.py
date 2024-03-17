# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if curr == None:
                return head
            curr = curr.next

        nextHead = curr
        prev, curr, next = None, head, head.next
        for _ in range(k-1):
            prev, curr, next = curr, next, next.next
            curr.next = prev
        # curr.next = prev
        head.next = self.reverseKGroup(nextHead, k)
        return curr
