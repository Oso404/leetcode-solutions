"""
two pointer algo
suppose we have two heights: 3 and 9....we want to keep 9 and not 3...moving away from 9 would reduce width and height
key: move pointer with smallest height
keywords: "max area" --> giveaway for two pointers algorithm
"""
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l = 0
        r = len(heights)-1
        ar = 0
        while l < r:
            if(heights[l] < heights[r]):
                ca = (r-l) * (heights[l])
                l+=1
            else: #both heights are equal or r is smaller
                ca = (r-l) * (heights[r])
                r-=1
            ar = max(ar,ca)
        return ar
        
        