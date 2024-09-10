class Solution:
    def removeStars(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if s[i] == '*':
                res = res[:-1] 
                i += 1 
            else:
                res += s[i]
                i += 1
        return res