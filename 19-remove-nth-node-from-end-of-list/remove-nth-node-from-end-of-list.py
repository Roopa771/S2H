class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # dummy node to handle edge cases
        fast = slow = dummy
        
        # Step 1: Move fast n+1 steps ahead
        for _ in range(n+1):
            fast = fast.next
        
        # Step 2: Move both until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Step 3: Remove target node
        slow.next = slow.next.next
        
        return dummy.next
