class Solution:
    def minArray(self, numbers):
        if not numbers: return
        l, r = 0, len(numbers) - 1
        while l < r:
            m = l + ((r - l) >> 1)
            if numbers[m] > numbers[r]: l = m + 1
            elif numbers[m] < numbers[r]: r = m
            else: r -= 1
        return numbers[l]

    def minArray(self, numbers):
        for i in range(1, len(numbers)):
            if numbers[i-1] > numbers[i]:
                return numbers[i]
        return numbers[0]

