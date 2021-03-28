class Solution:
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
            if l1.val > l2.val:
                tHead.next = l2
                l2, tHead = l2.next, tHead.next
            else:
                tHead.next = l1
                l1, tHead = l1.next, tHead.next
        tHead.next = l1 if l1 else l2
        return dummy.next

