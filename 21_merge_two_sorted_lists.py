# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        if a is None and b is None:
            return None
        lst = []
        while a:
            lst.append(a.val)
            a = a.next
        while b:
            lst.append(b.val)
            b = b.next
        lst.sort()
        print(lst)
        final = ListNode(lst[0])
        head = final
        for ele in lst[1:]:
            final.next = ListNode(ele)
            final = final.next
        return head
        # if a is None and b is None:
        #     return None
        # print(final.val,final.next.val,final.next.next)
        # a = a.next
        # b = b.next
        # while a:
        #     while b:
        #         print('fv')
        #         if a and b and a.val < b.val:
        #             final = ListNode(val=a.val)
        #             final = final.next
        #             a = a.next
        #         elif a and b and a.val > b.val:
        #             final = ListNode(val=b.val)
        #             final = final.next
        #             b = b.next   
        #             break
        # return head
