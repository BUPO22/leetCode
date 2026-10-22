# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        temphead = ListNode(0)
        crnt = temphead
        over = 0
        while l1 or l2 or over:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            over, inval = divmod(num1 + num2 + over ,10)
            crnt.next = ListNode(inval)
            crnt = crnt.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return temphead.next