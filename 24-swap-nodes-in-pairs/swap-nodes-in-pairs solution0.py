# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        curr = head.next
        nextHead = curr.next
        curr.next = head
        head = curr
        while nextHead != None and nextHead.next != None:
            curr.next.next = nextHead.next
            curr = nextHead.next
            nextnextHead = curr.next
            curr.next = nextHead
            nextHead = nextnextHead
        curr.next.next = nextHead
        return head
