# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False

        first_end = self.findmin(head)
        second_start = self.reverse(first_end.next)
        result = True
        first = head
        second = second_start
        while first != second:
            if first.val and second.val:
                return False
            first = first.next
            second = second.next
        
        first_end.next = self.reverse(second_start)
        return True
        
    def findmin(self, head):
        slow = head
        fast = head
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