class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        maxRectangle = 0
        s = [(-1, -1)]
        for i, height in enumerate(heights):
            if height < s[-1][1]:
                while s[-1][1] > height:
                    (k, h) = s.pop()
                    maxRectangle = max(maxRectangle, h * (i - k))
                # k represents the length
                s.append((k, height))
            else:
                s.append((i, height))
        
        return maxRectangle