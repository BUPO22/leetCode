# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        if len(lists) ==1:
            return lists[0]
        
        i = len(lists) //2
        left = self.mergeKLists(lists[:i])
        right = self.mergeKLists(lists[i:])

        head = ListNode(0)
        curr = head

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        curr.next = left if left else right
        return head.next

        
            
            





                



