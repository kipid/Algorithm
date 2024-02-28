# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = list0 = ListNode()
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                list0.next = list1
                list0 = list1
                list1 = list1.next
            else:
                list0.next = list2
                list0 = list2
                list2 = list2.next
        while list1 != None:
            list0.next = list1
            list0 = list1
            list1 = list1.next
        while list2 != None:
            list0.next = list2
            list0 = list2
            list2 = list2.next
        return head.next