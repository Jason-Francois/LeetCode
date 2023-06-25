# Key: For any given i,
#   the product of all other element in the array = (product of elems to the left of arr[i]) * (product of elems to the right of arr[i])
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prodTable = {}
        for i in range(0, len(nums)):
            prodTable[i] = {"leftProduct": 1, "rightProduct": 1}

        # For any element, x, find the product of all elements to the left of x and
        # the product of all elements to the right of x.
        # Then for each element, multiply the left and right products together
        for i in range(0, len(nums)):
            if i != 0:
                prodTable[i]["leftProduct"] = prodTable[i -
                                                        1]["leftProduct"] * nums[i - 1]
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                prodTable[i]["rightProduct"] = prodTable[i +
                                                         1]["rightProduct"] * nums[i + 1]
        result = [prodTable[idx]["leftProduct"] * prodTable[idx]["rightProduct"]
                  for idx, _ in enumerate(nums)]
        return result

    # Time Complexity: O(n), loops through input array twice
    def productExceptSelfOptimalMethod(self, nums):
        result = [1] * (len(nums))
        prefix = 1
        # In-order traversal, for every element, calculate the product of all elements to the left of it
        for i in range(0, len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1

        # Reverse order traversal, multiply each element in the result array by the product of the elements that are to the right of it
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.productExceptSelfOptimalMethod(nums))
