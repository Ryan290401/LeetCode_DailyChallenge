class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head, val)

        # mid node
        slow = head
        fast = head
        prev = None

        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 1 2 3 4 5
        # 1 2   4 5

        if prev is not None:
            prev.next = None

        node = TreeNode(slow,val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)

        return node