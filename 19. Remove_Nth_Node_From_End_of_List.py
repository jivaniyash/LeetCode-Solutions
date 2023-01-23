# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Solution

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            head = None
            return head
        c = 0
        a = head
        while a:
            c += 1
            a = a.next
        a = head
        if c == n:
            return head.next
        for _ in range(c-n-1):
            a = a.next
        a.next = a.next.next if a.next.next else None
        return head
