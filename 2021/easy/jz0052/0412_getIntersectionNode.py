class Solution:
    # 哈希，存储A, 遍历B, 找到相同节点即返回
    def getIntersectionNode(self, headA, headB):
        tNodeA, tNodeB, Node_set = headA, headB, set()
        while tNodeA:
            Node_set.add(tNodeA)
            tNodeA = tNodeA.next
        while tNodeB:
            if tNodeB in Node_set:
                return tNodeB
            tNodeB = tNodeB.next
        return None


    # 设置不同的起点，使得从起点开始，两链表长度一致
    def getIntersectionNode(self, headA, headB):
        tmpA = dummyA = headA
        tmpB = dummyB = headB
        while tmpA and tmpB: tmpA, tmpB = tmpA.next, tmpB.next
        while tmpA: tmpA, dummyA = tmpA.next, dummyA.next
        while tmpB: tmpB, dummyB = tmpB.next, dummyB.next
        while dummyA:
            if dummyA == dummyB: return dummyA
            dummyA, dummyB = dummyA.next, dummyB.next
        return None


    # 双指针遍历两个链表长度和的长度，最终双指针将在共同结点处相遇, 
    # 如果没有共同结点，将遍历到最后None, 并满足条件退出
    def getIntersectionNode(self, headA, headB):
        tmpA, tmpB = headA, headB
        while tmpA != tmpB:
            tmpA = tmpA.next if tmpA else headB
            tmpB = tmpB.next if tmpB else headA
        return tmpA
