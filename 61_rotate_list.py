# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = head
        if head is None or head.next is None or k == 0:
            return head
        l = 0
        while a:
            b = a
            a = a.next
            l += 1
        temp = head
        a = head
        if l == k:
            return a
        else:
            count = k%l
            if count == 0:
                return a
            for _ in range(l-count-1):
                a = a.next
            c = a.next
            a.next = None
            head = c
            a = head
            while a and a.next:
                a = a.next
            a.next = temp            
        return head


