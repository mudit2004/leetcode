class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openB = 0
        closeB = 0 
        for i in s:
            if i == '(':
                openB += 1
            elif i == ')' and openB > 0:
                openB -= 1
            else:
                closeB += 1
        return abs(openB+closeB)

        