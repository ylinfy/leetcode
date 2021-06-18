class Solution:
    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    # 计数排序，类布隆, time: N
    def getLeastNumbers(self, arr, k):
        if k <= 0: return []
        if k >= len(arr): return arr
        nums = [0] * 10000  # 当arr中数值有边界[0,10000]时，可以用此方法，nums索引值为arr中元素
        for e in arr: nums[e] += 1  # 统计arr中各元素出现的次数，如果arr中有n，则最终nums[n] >= 1
        i, res = 0, []
        while len(res) < k:
            if nums[i] >= 1:  # 说明arr中有元素i, 取最小topK，正序遍历nums, 直接满足条件的值等于k个，若取最大topK, 则倒序遍历nums
                for _ in range(nums[i]):  # 看看arr中有多少个元素i
                    if len(res) == k: break
                    res.append(i)
            i += 1
        return res


    # quick_sort, time: N*logN
    def getLeastNumbers(self, arr, k):
        if k <= 0: return []
        if k >= len(arr): return arr
        self.quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    def quick_sort(self, arr, l, r):
        if l >= r: return 
        i, j = l, r
        while i < j:
            # 将arr[l]设置为哨兵，遍历一次后，比哨兵大的在右边，比哨兵小的在左边
            # i < j不能带有=号，否则会出现索引越界的情况：i = j = 0, j -= 1即越界
            # arr[i/j] >= arr[l]不能没有=号，否则会死循环：[1,2,1]
            while i < j and arr[j] >= arr[l]: j -= 1
            while i < j and arr[i] <= arr[l]: i += 1
            self.swap(arr, i, j)
        self.swap(arr, i, l)
        self.quick_sort(arr, l, i - 1)
        self.quick_sort(arr, i + 1, r)


    # quick_sort II, time: N (N + N/2 + N/4 + ...) -> 小于2N, 即O(N)
    # 取最小topK，遇到左区间长度刚好为k时，直接返回左区间即可
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
        # 若左区间长度i, 若k==i，即左区间刚好是最小topK, 若k<i,只需遍历左区间，否则，只遍历右区间
        if k == i: return
        elif k < i: self.quick_sort(arr, l, i - 1, k)
        else: self.quick_sort(arr, i + 1, r, k)
    

    # merge_sort, 不适用于此题，适用于计算逆序对等类题
    # time: N*logN
    def getLeastNumbers(self, arr, k):
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
        tmp = []
        i, j = l, m + 1
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
        # 区间排好序的结果tmp，赋给对应arr区间
        arr[l:r+1] = tmp

    
    # 大顶堆，time: Nlogk
    # 最小topK用大顶堆，最大topK用小顶堆
    def getLeastNumbers(self, arr, k):
        if k <= 0: return []
        if k >= len(arr): return arr
        heap = arr[:k]
        self.build_heap(heap)
        for i in range(k, len(arr)):
            if arr[i] < heap[0]:  # 比大顶堆的根元素小，替换，保证堆中元素是最小topK
                heap[0] = arr[i]
                # 替换后，做一次heapify_down
                self.heapify_down(heap, 0)
        return res

    # 用数组构造大顶堆
    def build_heap(self, hlist):
        idx = len(hlist) - 1  # 最后节点的索引
        last_father = (idx - 1) // 2  # 最后节点父节点的索引 (自身索引 - 1) // 2
        # 从最后节点父节点开始构建
        for i in range(last_father, -1, -1):
            self.heapify_down(hlist, i)

    # heapify_down
    def heapify_down(self, hlist, idx):
        l, r = idx * 2 + 1, idx * 2 + 2  # 求出左右儿子节点的索引
        ma = idx  # 初始化父节点为最大值
        if l < len(hlist) and hlist[l] > hlist[ma]: ma = l
        if r < len(hlist) and hlist[r] > hlist[ma]: ma = r
        if ma != idx:  # 三者间最大值另有其人，将最大值与父节点交换
            self.swap(hlist, ma, idx)
            self.heapify_down(hlist, ma)

    # heapify_up, 此题用不着
    def heapify_up(self, hlist, idx):
        fa = (idx - 1) // 2  # 找到父节点
        if fa >= 0 and hlist[idx] > hlist[fa]:
            self.swap(hlist, idx, fa)
            self.heapify_up(hlist, fa)
            
                    
                

