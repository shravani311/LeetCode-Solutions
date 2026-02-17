class Solution:
    def containsDuplicate(self, nums: List[int]):
        s=set(nums)
        l=list(nums)
        if len(s)==len(l):
            return False
        else:
            return True