#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#先申请一个数组，然后遍历链表，把链表的值放入数组中，再反转数组，最后遍历链表赋值
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        while cur:
        	# 记录当前节点的下一个节点
        	tmp = cur.next
        	# 然后将当前节点指向pre
        	cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre

    def reverseList1(self, head: ListNode) -> ListNode:
        # 递归终止条件是当前为空，或者下一个节点为空
        if head == None or head.next == None:
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList1(head.next)
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
		# 而head是4，head的下一个是5，下下一个是空
		# 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur
# @lc code=end