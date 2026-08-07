class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix 
        self.prefixMatrixSums = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix)+1)]
        for i in range(1, len(matrix) + 1):
            prefix = 0 
            for j in range(1, len(matrix[0]) + 1):
                prefix += matrix[i - 1][j - 1] 
                self.prefixMatrixSums[i][j] = prefix + self.prefixMatrixSums[i -1][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefixMatrixSums[row2 + 1][col2 + 1]
        top = self.prefixMatrixSums[row1][col2 + 1]
        left = self.prefixMatrixSums[row2 + 1][col1]
        corner = self.prefixMatrixSums[row1][col1]
        return total - top - left + corner
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)