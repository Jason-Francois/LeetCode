class Solution(object):
    # Time Complexity: O(n), only loop through the array once\
    # Space Complexity: O(n), in the worst case, the hash map contains all the values of the arrays as keys
    # Approach: Iterate through the list once, using a hash map to keep track of previously seen values
    # For any current elem, if the number needed to get to the target is in the hash map get the
    # index of that number from the hashmap and return an array [that index,currentIndex]
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}  # maps val  -> index
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff], idx]
            else:
                prevMap[val] = idx


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))
