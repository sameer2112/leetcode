class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = len(nums)
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d.get(i,0) > (a//2):
                return i