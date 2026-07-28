class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        l = 0
        r = len(heights) - 1
        bestArea = 0

        while(l < r):
            currArea = (r - l) * min(heights[r], heights[l])
            bestArea = max(bestArea, currArea)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return bestArea

        
        
                    