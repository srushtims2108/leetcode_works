class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        current = head
        len = 1
        while current.next != None:
            len += 1
            current = current.next

        # Make list circular
        current.next = head

        # Adjust k (handle k > len)
        k = k % len
        if k == 0:
            current.next = None
            return head

        # Move (len - k) steps to find new tail
        steps = len - k
        for i in range(steps):
            current = current.next

        # Break the list and set new head
        new_head = current.next
        current.next = None

        return new_head
