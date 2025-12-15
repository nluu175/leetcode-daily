class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        counter = 0
        periodStart = 0
        
        for i in range(len(prices) - 1):
            print(i, periodStart)

            if prices[i] - 1 == prices[i + 1]:
                continue
            else:
                length = i - periodStart + 1
                counter += (length * (length + 1)) // 2     # This will never generate decimal since its the product of 2 consecutive numbers
                periodStart = i + 1 

        # Add the final period
        length = len(prices) - periodStart
        counter += (length * (length + 1)) // 2
        
        return counter

def main():
    sol = Solution()

    prices = [3, 2, 1, 4]
    res = sol.getDescentPeriods(prices)

    print(res)