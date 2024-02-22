# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = l1.val + l2.val
        res = ListNode(sum % 10)
        res1 = res
        while l1.next != None or l2.next != None or sum // 10 != 0:
            if l1.next == None:
                valL1 = 0
            else:
                l1 = l1.next
                valL1 = l1.val
            if l2.next == None:
                valL2 = 0
            else:
                l2 = l2.next
                valL2 = l2.val
            sum = valL1 + valL2 + sum // 10
            res1.next = ListNode(sum % 10)
            res1 = res1.next
        return res
