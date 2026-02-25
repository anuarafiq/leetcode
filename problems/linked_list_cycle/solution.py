# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        if not ptr or not ptr.next: return False

        while ptr.next and ptr.next.next:
            if ptr == ptr.next: return True
            ptr = ptr.next
            ptr.next = ptr.next.next 

        return False