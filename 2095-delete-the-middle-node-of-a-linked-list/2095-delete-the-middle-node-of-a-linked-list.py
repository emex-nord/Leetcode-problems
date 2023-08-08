# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head,head
        
        while fast and fast.next:
            fast = fast.next.next
            prevNode = slow
            slow = slow.next
        
        if slow == head:
            head = None
        else:
            prevNode.next = slow.next
            return head