class Soluttion:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                ret[j] += ret[j - 1]
        return ret
