import math
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert nums to a max heap by using negative values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        total = 0
        
        for _ in range(k):
            # Get the maximum element (invert the negative sign)
            max_element = -heapq.heappop(max_heap)
            total += max_element
            # Add the reduced element back to the heap
            new_value = math.ceil(max_element / 3)
            heapq.heappush(max_heap, -new_value)
        
        return total