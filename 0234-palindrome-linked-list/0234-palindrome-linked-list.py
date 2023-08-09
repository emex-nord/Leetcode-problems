# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prevNode = None
        while slow:
            nextNode = slow.next
            slow.next = prevNode
            prevNode = slow
            slow = nextNode
            
        current = head
        while prevNode:
            if prevNode.val != current.val:
                return False
            else:
                prevNode = prevNode.next
                current = current.next
        return True
                