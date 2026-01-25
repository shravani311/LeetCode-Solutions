class Solution:
    def removeDuplicates(self, nums: List[int]):
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
        for i in range(len(a)):
            nums[i]=a[i]
        return len(a)
        