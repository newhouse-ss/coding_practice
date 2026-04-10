class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 显然这题是不定长的滑动窗口
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # can not get profit currently, move l to r get higher profit.
                l = r
            r += 1
        return maxP