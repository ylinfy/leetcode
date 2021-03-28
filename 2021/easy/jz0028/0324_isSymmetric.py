class Solution: 
    # 递归，time: N
    # 根据对称性，逐一比较以根节点为中心左右对称的节点
    def isSymmetric(self, root):
        if not root: return True
        return self.comp(root.left, root.right)

    def comp(self, L, R):
        # 左右子节点均为None，即此分支遍历到底了，且完全对称
        if L is None and R is None: return True
        # 左右子节点有一个为None, 即左右不对称，直接返回False
        if L is None or R is None: return False
        # 左右子节点val不相等，直接提前返回False，如果相等，继续比较下一对称节点
        return L.val == R.val and self.comp(L.left, R.right) and self.comp(R.left, L.right)



    # 辅助队列, time: N
    # 和递归一样，每次把对称的节点存储起来进行比较
    def isSymmetric(self, root):
        if not root: return True
        queue = collections.deque([root.left, root.right])
        while queue:
            L = queue.popleft()
            R = queue.pop()
            # 和递归不一样，递归是回溯到上一层，所以用return True, 此处只是比较完了一个分支, 用continue，继续比较其他分支
            if L is None and R is None: continue

            # 有不对称节点，直接返回False
            if L is None or R is None: return False
            if L.val != R.val: return False

            # 按左，右对称节点依次存入queue中
            queue.appendleft(L.left)
            queue.appendleft(R.left)
            queue.append(R.right)
            queue.append(L.right)
        return True


    
