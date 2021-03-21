class Solution:
    # 快慢指针，间隔k, 当快指针指向尾时，即返回slow
    # time: N, space: 1
    def getKthFromEnd(self, head, k):
        slow = fast = head
        for _ in range(k):
            fast = fast.next  # 找到第k个
        while fast:
            slow, fast = slow.next, fast.next
        return slow


    # 辅助栈，遍历时，记录链表的长度，返回倒数第k个即可
    def getKthFromEnd(self, head, k):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        return stack[- k] if len(stack) >= k else None

