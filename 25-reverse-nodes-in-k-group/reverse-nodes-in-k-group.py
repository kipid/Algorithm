# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        lessThanK = False
        lis = []
        for _ in range(k):
            lis.append(curr)
            if curr == None:
                lessThanK = True
                break
            curr = curr.next
        if lessThanK:
            return head
        
        temp = lis[k-1].next
        for i in range(k-1,0,-1):
            lis[i].next = lis[i-1]
        lis[0].next = self.reverseKGroup(temp, k)
        return lis[k-1]
