#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node
    
    def swapPairs1(self, head: ListNode) -> ListNode:
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a, b = c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next
# @lc code=end