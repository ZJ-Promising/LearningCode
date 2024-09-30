class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str1 = str(self.shu_zi(l1) + self.shu_zi(l2))
        head = ListNode()
        for i in str1:
            temp = ListNode(int(i))
            temp.next = head.next
            head.next = temp
        return head.next

    def shu_zi(self, node):
        zi_fu = ""
        if not node:
            return 0
        while node:
            zi_fu += str(node.val)
            node = node.next
        return int(zi_fu[::-1])
