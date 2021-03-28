class Solution:
    # 双指针，time: N
    # 把链表看作: None, head, head.next,...None
    # 初始化，pre, cur分别指向前面的None和head
    def reverseList(self, head):
        if not head: return head
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    # 递归，time: N
    # 和双指针一个意思，将双指针传入递归函数
    def reverseList(self, head):
        def recur(pre, cur):
            # 找到最后节点，返回给res
            if not cur: return pre
            res = recur(cur, cur.next)
            # 回溯时，将当前节点指向前一节点，实现反转
            cur.next = pre
            # res为最后节点，继续返回
            return res
        return recur(None, head)


    # 递归，time: N
    # 递归到最后节点，回溯时，反转，并将前面节点指向None
    def reverseList(self, head):
        if not head or not head.next: return head
        # DFS到最后节点，赋值给res
        res = self.reverseList(head.next)
        # 回溯时将当前节点的下一节点的下一节点指向自己，再将当前节点的下一节点指向None, 即实现两两反转
        head.next.next = head
        head.next = None
        return res
        
