# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        a = head
        while a:
            b = a
            a = a.next
            while a and b.val == a.val:
                if a:
                    a = a.next
                    b.next = a
                else:
                    return t
        return t            