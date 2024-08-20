class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sums = [0] * (n + 1)
        
        # Calculate suffix sums
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
        
        memo = [[0] * (n + 1) for _ in range(n)]
        
        # Function to determine the maximum stones Alice can get
        def max_stones_for_alice(m: int, i: int) -> int:
            if i >= n:
                return 0
            if memo[i][m] != 0:
                return memo[i][m]
            max_stones = 0
            for x in range(1, 2 * m + 1):
                opponent_stones = max_stones_for_alice(max(m, x), i + x)
                max_stones = max(max_stones, suffix_sums[i] - opponent_stones)
            memo[i][m] = max_stones
            return max_stones
        
        return max_stones_for_alice(1, 0)