# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums=[]
        for node in lists:
            while node:
                nums.append(node.val)
                node=node.next
        nums.sort()
        dummy=ListNode(0)
        curr=dummy
        for val in nums:
            curr.next=ListNode(val)
            curr=curr.next
        return dummy.next
            