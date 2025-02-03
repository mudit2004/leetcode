class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = 0

        for i in range(len(nums)):
            curr_length = 1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[j-1] :
                    curr_length += 1
                else:
                    break
            max_length = max(max_length , curr_length)

        for i in range(len(nums)):
            curr_length = 1
            for j in range(i+1,len(nums)):
                if nums[j] < nums[j-1] :
                    curr_length += 1
                else:
                    break
            max_length = max(max_length , curr_length)
        
        
        return max_length
        