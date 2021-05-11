class Solution:
    # 递归，time: M + N
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        tHead = dummy = ListNode(0)
        while l1 and l2:
            # 谁小就把谁赋给tHead
            if l1.val > l2.val:
                tHead.next = l2
                l2 = l2.next
            else:
                tHead.next = l1
                l1 = l1.next
            tHead = tHead.next
        # 把剩余的l1或者l2全部添加到tHead后面
        tHead.next = l1 if l1 else l2
        return dummy.next
