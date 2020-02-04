class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        max_left = [height[0]] * len(height)
        max_right = [height[-1]] *len(height)
        
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
         
        water = 0
        for i in range(len(height)):
            water += min(max_left[i], max_right[i]) - height[i]
        return water