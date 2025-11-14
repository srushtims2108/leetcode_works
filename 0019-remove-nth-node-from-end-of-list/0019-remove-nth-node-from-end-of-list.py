# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len=0       
        curr=head
        while curr:
            curr=curr.next
            len+=1
        dummy = ListNode(0, head)
        curr = dummy
        for _ in range(len - n):  # stop just before the node to delete
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next