# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l1 = head
        mid = self.findmin(l1)
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)
        self.merge(l1, l2)
        


    def findmin(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def merge(self, l1, l2):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next
            l1.next = l2
            l1 = l1_tmp
            l2.next = l1
            l2 = l2_tmp