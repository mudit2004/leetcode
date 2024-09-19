from functools import lru_cache
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        # Use an LRU cache to memoize results automatically
        @lru_cache(None)
        def compute(expr):
            # If the expression is a pure number, return it as a list
            if expr.isdigit():
                return [int(expr)]
            
            res = []
            
            # Iterate through the expression to find operators
            for i, char in enumerate(expr):
                if char in '+-*':  # If the character is an operator
                    # Recursively compute left and right sides
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    
                    # Compute results based on the operator
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
            
            return res
        
        # Call the helper function on the full expression
        return compute(expression)