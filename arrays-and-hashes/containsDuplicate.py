# Time Complexity: O(n) - Requires two iterations of the entire array (2n)
# Space Complexity: O(n) - Size of frequency table will grow with number of distinct elems in the array
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen_nums = {}

    # First pass, create freuqency table
    for num in nums:
        if num not in seen_nums:
            seen_nums[num] = 1
        else:
            seen_nums[num] += 1

    # Second pass, check for duplicates
    for _, value in seen_nums.items():
        if value > 1:
            return True
    return False


# Uses a set to keep track of duplicates as opposed to hash table (dict)
# Time Complexity: O(n) - only needs one iteration
# Space Complexity: O(n) - in the worst case, the hashset is the same size as the original array (all numbers are unique)


def containsDuplicateWithHashSet(nums):
    hashset = set()  # Lookup of values in set is O(1)
    for num in nums:
        if num not in hashset:
            hashset.add(num)
        else:
            return True
    return False


if __name__ == "__main__":
    test_case1 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    test_case2 = [1, 2, 3, 4]
    test_case3 = [1, 2, 3, 1]
    print(containsDuplicateWithHashSet(test_case2))
