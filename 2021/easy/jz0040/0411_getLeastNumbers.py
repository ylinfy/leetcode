class Solution:
    # 排序取前k个或者维护一个大小为k的堆
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    # 快排变体，快排时，某一区域左侧长度是k时，直接返回
    # time: N (N + N/2 + N/4 + ... + (N-1)/N) -> 2N, 即O(N)
    def getLeastNumbers(self, arr, k):
        if k <= 0: return []
        if k >= len(arr): return arr
        self.quick_sort(arr, 0, len(arr) - 1, k)
        return arr[:k]

    def quick_sort(self, arr, l, r, k):
        if l >= r: return
        i, j = l, r
        while i < j:
            while i < j and arr[j] >= arr[l]: j -= 1
            while i < j and arr[i] <= arr[l]: i += 1
            self.swap(arr, i, j)
        self.swap(arr, i, l)
        # 每次排好序后，比较i, k, 若递归到k==i, 直接返回, 若k小，只需要再递归左侧，若k大，则只递归右侧
        if k == i: return
        elif k > i: self.quick_sort(arr, i + 1, r, k)
        else: self.quick_sort(arr, l, i - 1, k)

            
    # 复习mergeSort, 可用于解决逆序对等问题, 在merge时，比较左右值，如果右值小于左值，则成为逆序对
    def getLeastNumbers(self, arr, k):
        if k <= 0: return []
        if k >= len(arr): return arr
        self.mergeSort(arr, 0, len(arr) - 1)
        return arr[:k]

    def mergeSort(self, arr, l, r):
        if l >= r: return
        m = l + ((r - l) >> 1)
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.merge(arr, l, m, r)
    
    def merge(self, arr, l, m, r):
        temp = []
        i, j = l, m + 1
        while i <= m and j <= r:
            if arr[i] > arr[j]:
                temp.append(arr[j])
                j += 1
            else:
                temp.append(arr[i])
                i += 1
        while i <= m:
            temp.append(arr[i])
            i += 1
        while j <= r:
            temp.append(arr[j])
            j += 1
        arr[l:r+1] = temp
            
            
    # 计数迭代，time: N
    # 由于题目中指明arr中元素在范围[0, 10000], 设置一个nums记录arr中各值的数量，遍历nums, 即可找出arr最小topK
    def getLeastNumbers(self, arr, k):
        if k <= 0: return []
        if k >= len(arr): return arr
        nums, res = [0] * 10000, []
        for e in arr: nums[e] += 1
        for i, n in enumerate(nums):
            if n >= 1:
                for j in range(n): 
                    if len(res) >= k: return res
                    res.append(i)
                if len(res) >= k: return res


    # 大根堆实现，time: Nlogk     
    # 取最小topK用大根堆，取最大topK用小根堆
    # 调库一行命令实现：return heapq.nsmallest(k, arr)
    # 删除堆顶元素，就交换heap[0]和heap[-1], 然后从根节点开始进行一次heapify down操作
    # 添加元素，直接append在末尾，从末尾做一次heapify up操作
    def getLeastNumbers(self, arr, k):
        if k <= 0: return []
        if k >= len(arr): return arr
        heap = arr[:k]
        self.build_heap(heap)
        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                self.heapify_down(heap, 0)
        return heap

    def build_heap(self, heap):
        # 末节点的父节点索引: (索引-1)//2，即(len(heap)-1 - 1)//2化简len(heap)//2 - 1
        idx = len(heap) - 1
        for i in range((idx - 1) // 2, -1, -1):
            self.heapify_down(heap, i)

    def heapify_down(self, heap, i):
        l, r = 2*i + 1, 2*i + 2
        ma = i  # 初始化当前子树最大值索引(当前子树根节点)
        # 存在左子节点并且大于根节点，更新索引
        if l < len(heap) and heap[l] > heap[ma]: ma = l
        # 存在右子节点并且大于根节点，更新索引
        if r < len(heap) and heap[r] > heap[ma]: ma = r
        if ma != i:  # 调整当前子树为大顶堆
            # 更新子树根节点值, 将原本根节点值给到ma，然后再对ma(l or r)继续heapify,
            # 一直到叶子节点，即整个heapify down的过程
            self.swap(heap, i, ma)
            self.heapify_down(heap, ma)

    # heapify up, 此题用不到
    def heapify_up(self, heap, i):
        fa = (i - 1) // 2  # 父节点索引: (自身索引 - 1) // 2
        if fa >= 0 and head[i] > head[fa]:
            # 比父节点大，交换, 一直比较到根节点，即整个heapify up过程
            self.swap(heap, i, fa)
            self.heapify_up(heap, fa)
