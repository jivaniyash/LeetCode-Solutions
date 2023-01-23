# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        if a is None or a.next is None:
            return a
        x = temp = ListNode(None)
        while a:
            b = a
            a = a.next
            y = False
            while a and a.val == b.val:
                print('rw')
                a = a.next
                y = True
            if not y:
                f = b
                f.next = None
                temp.next = f
                print(temp)
                temp = temp.next
        return x.next