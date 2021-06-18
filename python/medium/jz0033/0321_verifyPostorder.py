class Solution:
    # 给定一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果，是返回True，否返回False
    # 假定每个数字都互不相同
    
    # 递归，根据后序遍历的特性，找到根节点，即nums[-1], 判断剩余数据是否符合后续遍历特性
    # time: N**2 (当树退化成链表时，最大时间复杂度N**2)
    def verifyPostorder(self, postorder):
        # i, j分别为树的后序遍历首尾索引，根据后序遍历特性，可以找到左右子树的后续遍历首尾索引
        # 依次递归，且满足二叉搜索树定义
        def judge(i, j):
            if i >= j: return True
            t = i  # 记录首索引，用于递归左子树, 用临时索引t去遍历 
            while postorder[t] < postorder[j]: t += 1  # 据左子树区小于根节点，找到分界点，划分左，右子树区间
            m = t  # 记录左，右子树分界点索引，用于划分左右子树，从而drill down下去
            while postorder[t] > postorder[j]: t += 1  # process current level, 所有右子树区数必须大于根节点
            # 满足条件t == j即右区都小于根节点，才进入下一层，
            return t == j and judge(i, m - 1) and judge(m, j - 1)
        # 递归函数，传入左，右索引
        return judge(0, len(postorder) - 1)


    # 单调递归栈，将后序遍历数组反转，得到根、右、左的遍历顺序，即可维护一个递增栈
    # 当遇到一个小于栈中元素的数据时，找到第一个大于该数据的栈中元素，即为该元素的根节点
    # time: N (最坏的情况，每个节点都要入栈出栈)
    def verifyPostorder(self, postorder):
        if not postorder: return True
        stack, root = [], float('inf')
        for i in range(len(postorder) - 1, -1, -1):
            # 如果root左子树所有节点大于本身(root)，直接返回False
            if postorder[i] > root: return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()  # 更新postorder[i]的最近根节点
            stack.append(postorder[i])
        return True  # 遍历完，都满足规则，即返回True
