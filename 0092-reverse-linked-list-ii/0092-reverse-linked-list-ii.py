# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        current_node = dummy_node
        for i in range(0, right):
            if i == left - 1 :
                before_left = current_node
                left_node = before_left.next
            current_node = current_node.next
        right_node = current_node
        right_next = right_node.next
        
        prev_node = right_next
        while left_node.next != right_next:
            next_node = left_node.next
            left_node.next = prev_node
            prev_node = left_node
            left_node = next_node
        before_left.next = left_node
        left_node.next = prev_node
        return dummy_node.next
    
        