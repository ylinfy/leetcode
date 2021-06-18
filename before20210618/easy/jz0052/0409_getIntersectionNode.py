class Solution:
    # 哈希，存储headA, 遍历headB, 返回相同的节点
    def getIntersectionNode(self, headA, headB):
        tmpA, tmpB, node_set = headA, headB, set()
        while tmpA:
            node_set.add(tmpA)
            tmpA = tmpA.next
        while tmpB:
            if tmpB in node_set:
                return tmpB
            tmpB = tmpB.next
        return None
    

    # 长短不一的两链表，设置不同的起点，使得它们一起到达终点
    def getIntersectionNode(self, headA, headB):
        tmpA = dummyA = headA
        tmpB = dummyB = headB
        while tmpA and tmpB: tmpA, tmpB = tmpA.next, tmpB.next
        while tmpA: tmpA, dummyA = tmpA.next, dummyA.next
        while tmpB: tmpB, dummyB = tmpB.next, dummyB.next
        while dummyA and dummyB: 
            if dummyA == dummyB: return dummyA
            dummyA, dummyB = dummyA.next, dummyB.next
        return None


    # 双指针，time: M + N
    def getIntersectionNode(self, headA, headB):
        tmpA, tmpB = headA, headB
        while tmpA != tmpB:
            tmpA = tmpA.next if tmpA else headB
            tmpB = tmpB.next if tmpB else headA
        return tmpA
