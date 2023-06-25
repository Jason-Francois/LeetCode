class Solution(object):

    # Two Sum where input arr is sorted in ascending order
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1

        while (l <= r):
            currentSum = numbers[l] + numbers[r]
            if currentSum == target:
                return [l + 1, r + 1]
            elif currentSum < target:
                l += 1
            else:
                r -= 1
        return []


if __name__ == "__main__":
    nums = [-1, 0]
    target = -1
    sol = Solution()
    print(sol.twoSum(nums, target))
