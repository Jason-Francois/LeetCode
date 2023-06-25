class Solution(object):

    # Time Complexity: O(n), each element in list is inserted and
    # removed from the stack at most once
    # Space Complexity O(n): Stack size can be as large as input array size

    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []

        # Use monotonic decreasing stack to find the next warmest day
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                topOfStack = stack.pop()
                result[topOfStack] = i - topOfStack
            stack.append(i)
        return result


if __name__ == "__main__":
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(temperatures))
