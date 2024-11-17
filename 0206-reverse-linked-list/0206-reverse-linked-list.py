class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize pointers
        prev = None  # Previous node starts as None
        curr = head  # Current node starts at the head

        while curr is not None:
            next_node = curr.next
            
            curr.next = prev
            

            prev = curr
            curr = next_node

        # prev is now the new head of the reversed list
        return prev