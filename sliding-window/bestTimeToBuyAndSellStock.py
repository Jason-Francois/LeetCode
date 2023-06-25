class Solution(object):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Keep track of lowest price seen as you iterate through the array
        # Calculate the profit between current and lowest price (if current is greater than lowest), 
        # and update the max result if needed
        # If price at prices[i] is lower than the current lowest day, update lowest day
        lowest = prices[0]
        maxResult = 0
        for i in range(0, len(prices)):
            if prices[i] < lowest:
                # If price at prices[i] is lower than the current lowest day, update lowest day
                lowest = prices[i]
            if prices[i] - lowest > maxResult:
                maxResult = prices[i] - lowest
        return maxResult
