# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                maxp += prices[i+1] - prices[i]
            # for j in range(i+1, len(prices)):
            #     if 
        return maxp


if __name__ == '__main__':
    nums = [7,1,5,3,6,4]
    # nums = [1,2,3,4,5]
    # nums = [7,6,4,3,1]
    s = Solution().maxProfit(nums)
    print(s)