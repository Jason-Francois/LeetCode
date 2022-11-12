class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Hash map to keep track of seen values
        hashMap = {}

        # For each value in the array,
        # if num needed to reach target sum has been seen
        # return the indices of current value and num
        # Else add current value to hashMap
        for index, num in enumerate(nums):
            x = target - num
            # If
            if x in hashMap:
                return [index, hashMap[x]]
            else:
                hashMap[num] = index


if __name__ == "__main__":
    solution = Solution()
    arr = [2, 5, 5, 2]
    target = 10
    print(solution.twoSum(arr, target))
