class Solution:
    def findContinousSequence(self, target):
        i, j, res = 1, 2, []
        while j <= target // 2 + 1:
            s = (i + j) * (j - i + 1) // 2
            if s < target: j += 1
            elif s > target: i += 1
            else:
                res.append(list(range(i, j + 1)))
                i += 1
        return res
    
    def findContinousSequence(self, target):
        d, res = 1, []
        while d * (d + 1)/ 2 < target:
            if not (target - d * (d + 1) // 2) % (d + 1):
                i = (target - d * (d + 1) // 2) // (d + 1)
                res.append(list(range(i, d + i + 1)))
            d += 1
        return res[::-1]
        
