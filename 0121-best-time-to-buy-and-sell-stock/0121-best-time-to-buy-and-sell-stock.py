class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        maximum = 0
        profit = 0
        for i in range(len(prices)):
            minimum = min(prices[i] , minimum)
            profit = max(profit , prices[i] - minimum)
        return profit