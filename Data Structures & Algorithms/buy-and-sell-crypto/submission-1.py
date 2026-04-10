class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 不定长滑动窗口
        n = len(prices)
        l = res = 0

        for r in range(n):
            if prices[l] < prices[r]:
                curr = prices[r]-prices[l]
                res = max(res, curr)
            else:
                l = r
        return res