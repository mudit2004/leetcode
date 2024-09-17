class Solution:
    def findMaxForm(self, strs: List[str], zeros: int, ones: int) -> int:
        encoding = [(x.count('0'), x.count('1')) for x in strs]
        dp = [[[-1 for _ in range(ones + 1)] for _ in range(zeros+1)] for _ in range(len(encoding) + 1)]
        def recursion(index, zeros, ones):
            if index == len(encoding):
                return 0
            if dp[index][zeros][ones] != -1:
                return dp[index][zeros][ones]
            notTake = recursion(index+1, zeros, ones)
            take = 0
            if zeros - encoding[index][0] >= 0 and ones - encoding[index][1] >= 0:
                take = recursion(index+1, zeros-encoding[index][0], ones-encoding[index][1]) + 1
            dp[index][zeros][ones] = max(notTake, take)
            return dp[index][zeros][ones]
        for i in range(zeros+1):
            for j in range(ones+1):
                dp[0][i][j] = 0
        for i in range(1,len(encoding) + 1):
            for j in range(0, zeros+1):
                for k in range(0, ones+1):
                    notTake = dp[i-1][j][k]
                    take = 0
                    if j - encoding[i-1][0] >= 0 and k - encoding[i-1][1] >= 0:
                        take = 1 + dp[i-1][j - encoding[i-1][0]][k - encoding[i-1][1]]
                    dp[i][j][k] = max(take, notTake)
        return dp[len(encoding)][zeros][ones]
        # return recursion(0,zeros, ones)