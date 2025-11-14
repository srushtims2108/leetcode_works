# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        value=set()
        current=head
        while current.next:
            if current in value:
                return True
            else:
                value.add(current)
            current=current.next
        return False
