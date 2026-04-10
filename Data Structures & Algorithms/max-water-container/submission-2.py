class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # The intuition is: The amount of water is determined by the short edge.
        # So we keep moving the short edge inner, aim to find larger amount of water.
        n = len(heights)
        res = 0

        left, right = 0, n-1
        while left < right:
            shorter = min(heights[left], heights[right]) #PITFALL: heights[i] is the height of wall.
            bottom = right - left
            res = max(res, shorter * bottom)

            # exlpore possibility to be larger.
            if shorter == heights[left]:
                left += 1
            else:
                right -= 1

        return res