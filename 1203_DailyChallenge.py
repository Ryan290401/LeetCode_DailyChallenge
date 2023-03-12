# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minval = float('inf')
        index = -1

        for i in range(len(lists)):
            if lists[i] == None:
                continue

            if lists[i].val < minval:
                index = i
                minval = lists[i].val

        if index == -1:
            return None

        node = lists[index]
        lists[index] = lists[index].next
        node.next = self.mergeKLists(lists)

        return node