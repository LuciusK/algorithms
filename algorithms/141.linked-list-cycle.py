#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #定义一个set，然后不断遍历链表
        s = set()
        while head:
            #如果某个节点在set中，说明遍历到重复元素了，也就是有环
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
    
    def hasCycle1(self, head: ListNode) -> bool:
        if not (head and head.next):
            return False
        #定义两个指针i和j，i为慢指针，j为快指针 
        i, j = head, head.next
        while j and j.next:
            if i == j:
                return True
            # i每次走一步，j每次走两步
            i, j = i.next, j.next.next
        return False
# @lc code=end