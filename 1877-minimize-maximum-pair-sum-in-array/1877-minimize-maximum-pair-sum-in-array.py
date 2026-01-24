class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        num=sorted(nums)
        n=len(nums)-1
        maximum=[]
        for i in range(n+1):
            maximum.append(num[i]+num[n-i])
        return max(maximum)