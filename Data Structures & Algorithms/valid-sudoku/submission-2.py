"""
Aim for solution good or better than O(n^2) time and space complexity 

We have to think about forming the board again. As we go through each value of each row, we form the columns and the squares. We check at each iteration if those are valid. So we would need to initalize a set for each row, each column, and each square. 

So let's say we go through the first row. This covers 3 things
1. The whole set() at index 0 of rows 
2. 3 column values, so set() at index 0, 1, 2 
3. 3 values of the box, so set at index 0

For the boxes we can assume 0 is top left, and 8 is bottom right 

To box these values, let's take an example. For example I want to insert 6 into box 4 (the center box). 6 is at row 3, col 4. The col at 4 gives us a good start, because 4 % 3 = 1. This would be the box that is above the box we want. So then, we have to adjust it by taking the row value, which is row 3. 1 + 3 * (3//3) = 4 which is correct. 
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(len(board))]
        cols = [set() for i in range(len(board))]
        squares = [set() for i in range(len(board))]
        
        for i in range(len(board)): 
            row = board[i] 
            for j in range(len(row)): 
                val = row[j]
                boxNum = (j//3) + (i//3) * 3
                if val != ".":
                    if val in rows[i] or val in cols[j] or val in squares[boxNum]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)    
                    squares[boxNum].add(val) 
        return True
