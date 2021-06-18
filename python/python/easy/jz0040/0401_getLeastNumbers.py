class Solution:
    # 可以使用arr.sort(), 后再返回前k个数, 算法工程师应该自己实现排序
    # quick sort, time: NlogN
    def getLeastNumbers(self, arr, k):
        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[l] = arr[l], arr[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)
        if len(arr) <= k: return arr
        quick_sort(0, len(arr) - 1)
        return arr[:k]


    # 快排时，某一区域左侧长度是k时，直接返回
    # time: N (N + N/2 + N/4 + ... + (N-1)/N) -> 2N, 即O(N)
    def getLeastNumbers(self, arr, k):
        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[l] = arr[l], arr[i]

            # 每次排好序后，比较i, k, 若刚好递归到k==i, 直接返回, 若k小，只需要再递归左侧，若k大，则只递归右侧
            if k == i: return
            elif k < i: quick_sort(l, i - 1)
            else: quick_sort(i + 1, r)

        if len(arr) <= k: return arr
        quick_sort(0, len(arr) - 1)
        return arr[:k]
            

    # 复习merge sort, time: NlogN
    def getLeastNumbers(self, arr, k):
        if len(arr) <= k: return arr
        self.merge_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    def merge_sort(self, arr, l, r):
        if l >= r: return 
        m = l + ((r - l) >> 1)
        self.merge_sort(arr, l, m)
        self.merge_sort(arr, m + 1, r)
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
        arr[l:r + 1] = temp
                
    
    # 计数排序，类布隆过滤器
    # time: N, 速度较快
    def getLeastNumbers(self, arr, k):
        nums = [0] * 10000
        for n in arr: nums[n] += 1  # 用nums索引n来记录arr中出现的n的个数
        i, res = 0, []
        while len(res) < k:
            if nums[i] >= 1: # 取arr中最小值，nums[i]为0时，代表arr中没有数值i
                for _ in range(nums[i]):
                    if len(res) == k: break
                    res.append(i)
            i += 1
        return res


    # 大根堆实现，time: Nlogk     
    # 取最小topK用大根堆，取最大topK用小根堆
    # 调库一行命令实现：return heapq.nsmallest(k, arr)
    # 删除堆顶元素，就交换heap[0]和heap[-1], 然后从根节点开始进行一次heapify down操作
    # 添加元素，直接append在末尾，从末尾做一次heapify up操作
    def getLeastNumbers(self, arr, k):
        if k == 0: return []
        if k >= len(arr): return arr
        heap = arr[:k]
        self.build_heap(heap)
        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                self.heapify_down(heap, 0)
        return heap

    @staticmethod
    def swap(heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]

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

    def build_heap(self, heap):
        # 末节点的父节点索引: (索引-1)//2，即(len(heap)-1 - 1)//2化简len(heap)//2 - 1
        for i in range(len(heap) // 2 - 1, -1, -1):
            self.heapify_down(heap, i)

    # heapify up, 此题用不到
    def heapify_up(self, heap, i):
        fa = (i - 1) // 2  # 父节点索引: (自身索引 - 1) // 2
        if fa >= 0 and head[i] > head[fa]:
            # 比父节点大，交换, 一直比较到根节点，即整个heapify up过程
            self.swap(heap, i, fa)
            self.heapify_up(heap, fa)
             









