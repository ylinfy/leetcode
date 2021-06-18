class Solution:
    # quick_sort, time: NlogN
    def getLeastNumbers(self, arr, k):
        if k <= 0: return []
        if k >= len(arr): return arr
        self.quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    def quick_sort(self, arr, l, r):
        if l >= r: return
        i, j = l, r
        while i < j:
            # arr[l] 即最左边数设置为哨兵，比哨兵大的放右边，比哨兵小的放左边
            # 找到右边第一个比哨兵arr[l]小的数，找到左边第一个比哨兵大的数，交换
            # 此处一定要用>=, <=，不带=号的话，像[1,2,1]这样的对称数,ij永远是0，2，就进入死循环了
            while i < j and arr[j] >= arr[l]: j -= 1
            while i < j and arr[i] <= arr[l]: i += 1
            arr[i], arr[j] = arr[j], arr[i]
        # 全部交换后，i索引所在的数，应该是最接近哨兵arr[l]但比其小的数，交换i,l
        # 即哨兵换到中间arr[i], 并且左边的都比它小, 右边的都比它大
        arr[i], arr[l] = arr[l], arr[i]
        # 递归左，右区间
        self.quick_sort(arr, l, i - 1)
        self.quick_sort(arr, i + 1, r)


    # quick_sort, time: N 
    # time: N (N + N/2 + N/4 + ... + (N-1)/N) -> 2N, 即O(N) (每次循环只走一个分支)
    # 由于是求最小topK, 某一次排序后，左边区间长度为k，即可提前终止
    def getLeastNumbers(self, arr, k):
        if k <= 0: return []
        if k >= len(arr): return arr
        self.quick_sort(arr, 0, len(arr) - 1, k)
        return arr[:k]

    def quick_sort(self, arr, l, r, k):
        if l >= r: return
        i, j = l, r
        while i < j:
            # arr[l] 即最左边数设置为哨兵，比哨兵大的放右边，比哨兵小的放左边
            # 找到右边第一个比哨兵arr[l]小的数，找到左边第一个比哨兵大的数，交换
            # 此处一定要用>=, <=，不带=号的话，像[1,2,1]这样的对称数,ij永远是0，2，就进入死循环了
            while i < j and arr[j] >= arr[l]: j -= 1
            while i < j and arr[i] <= arr[l]: i += 1
            arr[i], arr[j] = arr[j], arr[i]
        # 全部交换后，i索引所在的数，应该是最接近哨兵arr[l]但比其小的数，交换i,l
        # 即哨兵换到中间arr[i], 并且左边的都比它小, 右边的都比它大
        arr[i], arr[l] = arr[l], arr[i]
        # 递归左，右区间
        # 不用递归两个区间，判断左区间长度是否比k大, 大就只递归左区间，小说明左区间已经是topK最小了，只递归右区间继续找剩下的top(K - 左区间长度)
        if k == i: return  # 等于左区间长度，直接返回
        elif k < i: self.quick_sort(arr, l, i - 1, k)
        else: self.quick_sort(arr, i + 1, r, k)


    # 归并排序，time: NlogN
    # 适用于逆序对统计
    def getLeastNumbers(self, arr):
        if k <= 0: return [] 
        if k >= len(arr): return arr
        self.merge_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    def merge_sort(self, arr, l, r):
        if l >= r: return
        m = l + ((r - l) >> 1)
        self.merge_sort(arr, l, m)
        self.merge_sort(arr, m + 1, r)
        self.merge(arr, l, m, r)
    
    def merge(self, arr, l, m, r):
        i, j, tmp = l, m + 1, []
        while i <= m and j <= r:
            if arr[i] > arr[j]:
                tmp.append(arr[j])
                j += 1
            else:
                tmp.append(arr[i])
                i += 1
        while i <= m:
            tmp.append(arr[i])
            i += 1
        while j <= r:
            tmp.append(arr[j])
            j += 1
        arr[l:r+1] = tmp
            

    # 大顶堆（最小topK用大顶堆，最大topK用小顶堆）
    # 也可调用python库,一行代码搞定：return heapq.nsmallest(k, arr)
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

    @staticmethod
    def swap(heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]

    def build_heap(self, hlist):
        # 父节点索引: (索引-1)//2
        # 建立堆时，从最后非叶子节点开始遍历
        idx = len(hlist) - 1
        for i in range((idx - 1) // 2, -1, -1):
            self.heapify_down(hlist, i)
         
    def heapify_down(self, heap, idx):
        l, r = idx * 2 + 1, idx * 2 + 2
        ma = idx  # 初始化当前节点为该子树最大值
        # 存在左子节点并且大于最大值节点，更新最大值索引
        if l < len(heap) and heap[l] > heap[ma]: ma = l
        # 存在右子节点并且大于最大值节点，更新最大值索引
        if r < len(heap) and heap[r] > heap[ma]: ma = r
        if ma != idx:  # 说明当前节点并非该子树最大值
            # 更新子树根节点值, 将原本根节点值给到ma，然后再对ma(l or r)继续heapify,
            # 一直到叶子节点，即整个heapify down的过程
            self.swap(heap, ma, idx)
            self.heapify_down(heap, ma)
    
    def heapify_up(self, heap, idx):
        fa = (idx - 1) // 2  # 父节点索引: (自身索引 - 1) // 2
        if fa >= 0 and head[idx] > head[fa]:
            # 比父节点大，交换, 一直比较到根节点，即整个heapify up过程
            self.swap(heap, idx, fa)
            self.heapify_up(heap, fa)


    # 计数排序，类布隆
    def getLeastNumbers(self, arr, k):
        nums = [0] * 10000
        for n in arr: nums[n] += 1  # 用nums索引n来记录arr中出现的n的个数
        i, res = 0, []
        while len(res) < k:
            if nums[i] >= 1:
                for _ in range(nums[i]):  # 取arr中最小值，nums[i]为0时，代表arr中没有数值i
                    if len(res) == k: break
                    res.append(i)
            i += 1
        return res
