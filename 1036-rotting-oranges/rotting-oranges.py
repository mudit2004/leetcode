class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes_passed = 0
        
        while queue and fresh_oranges > 0:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 
                        fresh_oranges -= 1
                        queue.append((nx, ny))
        
        return -1 if fresh_oranges > 0 else minutes_passed