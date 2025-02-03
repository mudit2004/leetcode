class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        max_length = 0

        for i in range(n):
            for increasing in [True, False]:  # Check both increasing and decreasing
                curr_length = 0
                for j in range(i, n):
                    if j > i: #if not the first element of the sub-array
                        if increasing and nums[j] > nums[j-1]:
                            curr_length += 1
                        elif not increasing and nums[j] < nums[j-1]:
                            curr_length += 1
                        else:
                            break #break if the monotonicity is broken
                    else: #if the first element
                        curr_length = 1
                max_length = max(max_length, curr_length)

        return max_length