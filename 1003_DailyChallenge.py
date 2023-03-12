# Definition for singly-linked list.
# class ListNode
#     def __init__(self, val=0, next=None:
#         self.val = val
#         self.next = next
import random


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.haed = head

    def getRandom(self) -> int:
        curr = self.haed
        cnt = 0
        res = curr.val
        while curr:
            cnt += 1
            randomnum = random.randint(1,cnt)
            if randomnum == 1:
                res = curr.val
            curr = curr.next
        return res