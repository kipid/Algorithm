# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        next = head
        count = 1
        while (next := (last := next).next) != None:
            count += 1
        until = count - (k % count)
        last.next = head
        print(f"{count = }, {until = }")
        for _ in range(until):
            last, head = head, head.next
        last.next = None
        return head