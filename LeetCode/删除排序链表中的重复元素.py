# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre = head
        p = pre.next
        while p:
            if p.val != pre.val:
                pre = pre.next
            else:
                pre.next = p.next
            p = p.next
        return head
