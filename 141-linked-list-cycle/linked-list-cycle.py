# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict_ = dict()
        dict_[head] = True
        curr = head
        while curr and (curr := curr.next):
            dict_[curr] = True
            if curr.next in dict_:
                return True
        return False