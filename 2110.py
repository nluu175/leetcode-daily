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

    def getDescentPeriods_DP(self, prices: List[int]) -> int:
        """
        LeetCode categorizes this one as DP problem, so I gave it a try
        """
        n = len(prices)
        if n == 0:
            return 0

        counter = 0
        dp = 1  # Length of period ending at current position
        counter += 1  # First element contributes 1

        for i in range(1, n):
            if prices[i - 1] - 1 == prices[i]:
                dp = dp + 1  # Extend the streak
            else:
                dp = 1  # Reset to new period

            counter += dp  # Add the length (counts all periods ending here)

        return counter

def main():
    sol = Solution()

    prices = [3, 2, 1, 4]
    res = sol.getDescentPeriods(prices)

    print(res)