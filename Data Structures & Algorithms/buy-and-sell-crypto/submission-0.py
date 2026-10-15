class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        max_so_far = 0
        end_index = len(prices) - 1

        while R <= end_index:
            if prices[L] <= prices[R]:
                profit = prices[R] - prices[L]
                max_so_far = max(max_so_far, profit)
            else: # L < R
                L = R
            R += 1

        return max_so_far