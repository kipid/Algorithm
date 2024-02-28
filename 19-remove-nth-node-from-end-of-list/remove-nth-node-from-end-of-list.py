# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_ = [head]
        curr = head
        while (curr := curr.next) != None:
            list_.append(curr)
        if n == len(list_):
            head = head.next
            list_[0].next = None
        elif n == 1:
            list_[len(list_)-2].next = None
        else:
            list_[len(list_)-n-1].next = list_[len(list_)-n+1]
        return head