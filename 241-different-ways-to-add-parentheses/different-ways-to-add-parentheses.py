from functools import lru_cache
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def compute(expr):
            if expr.isdigit():
                return [int(expr)]
            res = []
            for i, char in enumerate(expr):
                if char in '+-*': 
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
            return res
        return compute(expression)