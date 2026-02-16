class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_min=float('inf')
        curr_max=0
        for i in range(len(prices)):
            if last_min>prices[i]:
                last_min=prices[i]
            if (prices[i]-last_min)>curr_max:
                curr_max=prices[i]-last_min
        return curr_max
