class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        two pointers: Start with the widest container.
        Notice the volume of the container is limited by the 
        short edge, thus we need to move the shorter edge inword
        to persue larger volume, moving the higher edge helps
        nothing and the width is decreased.
        """
        left = 0
        right = len(heights) - 1
        res = 0

        while left<right:
            res = max(res, (right-left)*min(heights[left], heights[right]))
            if heights[left]<heights[right]:
                left += 1
            else:
                right -= 1
        
        return res
