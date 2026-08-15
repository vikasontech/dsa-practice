'''
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        a = prices
        profit = 0
        while r < len(a):
            if a[l] > a[r]:
                l = r
                r += 1
            else:
                profit = max(profit, a[r]-a[l])
                r += 1
        return profit

s = Solution()

print('Profit: ', s.maxProfit([8, 3,7,1,5,2,6,4]))
print('Profit: ', s.maxProfit([7,1,5,3,6,4]))
print('Profit: ', s.maxProfit([7,6,4,3,1]))
print('Profit: ', s.maxProfit([1]))
print('Profit: ', s.maxProfit([2,4,1]))
print('Profit: ', s.maxProfit([2,1,2,1,0,1,2]))


