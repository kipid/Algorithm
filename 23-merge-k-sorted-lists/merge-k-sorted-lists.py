# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            head = sorted_ = ListNode()
            while lists[0] != None and lists[1] != None:
                if lists[0].val <= lists[1].val:
                    sorted_.next = lists[0]
                    sorted_ = lists[0]
                    lists[0] = lists[0].next
                else:
                    sorted_.next = lists[1]
                    sorted_ = lists[1]
                    lists[1] = lists[1].next
            while lists[0] != None:
                sorted_.next = lists[0]
                sorted_ = lists[0]
                lists[0] = lists[0].next
            while lists[1] != None:
                sorted_.next = lists[1]
                sorted_ = lists[1]
                lists[1] = lists[1].next
            return head.next
        else:
            return self.mergeKLists([self.mergeKLists(lists[:(len(lists)//2)]), self.mergeKLists(lists[(len(lists)//2):])])