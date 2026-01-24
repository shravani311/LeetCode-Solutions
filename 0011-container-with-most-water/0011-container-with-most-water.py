class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        maximum=[]
        left_index=0
        right_index=n-1
        while left_index<right_index:
            minimum=min([height[left_index],height[right_index]])
            dist=minimum*(right_index-left_index)
            maximum.append(dist)
            if height[left_index]<height[right_index]:
                left_index+=1
            else:
                right_index-=1
        return max(maximum)