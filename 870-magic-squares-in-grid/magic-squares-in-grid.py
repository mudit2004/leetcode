class Solution:
    def isMagicSquare(self, grid: List[List[int]], row: int, col: int) -> bool:
        s = {grid[row+i][col+j] for i in range(3) for j in range(3)}
        print(s)
        if s != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False
        magic_sum = 15
        return (sum(grid[row][col:col+3]) == magic_sum and
                sum(grid[row+1][col:col+3]) == magic_sum and
                sum(grid[row+2][col:col+3]) == magic_sum and
                sum(grid[row+i][col] for i in range(3)) == magic_sum and
                sum(grid[row+i][col+1] for i in range(3)) == magic_sum and
                sum(grid[row+i][col+2] for i in range(3)) == magic_sum and
                grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2] == magic_sum and
                grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col] == magic_sum)
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for row in range(rows - 2):
            for col in range(cols - 2):
                if self.isMagicSquare(grid, row, col):
                    count += 1

        return count