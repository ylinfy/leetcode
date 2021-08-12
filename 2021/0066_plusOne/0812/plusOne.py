class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0: return digits
        return [1] + digits
