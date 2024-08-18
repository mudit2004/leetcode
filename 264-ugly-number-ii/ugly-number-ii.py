import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        heapq.heapify(ugly_numbers)
        seen = set(ugly_numbers)

        factors = [2, 3, 5]

        for _ in range(1, n):
            min_ugly = heapq.heappop(ugly_numbers)
            for factor in factors:
                new_ugly = min_ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(ugly_numbers, new_ugly)

        return heapq.heappop(ugly_numbers)