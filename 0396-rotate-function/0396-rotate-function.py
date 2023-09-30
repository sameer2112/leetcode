class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        tot_sum  = sum(nums)
        curr_sum= 0
        for i in range(len(nums)):
            curr_sum = curr_sum+(i*nums[i])
        max_sum = curr_sum
        for  i  in range(1,len(nums)):
            curr_sum = curr_sum + tot_sum - n*nums[n-i]
            max_sum = max(max_sum,curr_sum)
        return max_sum

        
      

