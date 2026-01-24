class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1+=nums2
        nums1.sort()
        if len(nums1)%2==0:
            idx=int(len(nums1)/2)-1
            median=(nums1[idx]+nums1[idx+1])/2
            return median
        else:
            idx=int((len(nums1)-1)/2)
            return nums1[idx]