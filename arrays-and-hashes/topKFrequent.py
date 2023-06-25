import heapq


class Solution(object):
    # Time Complexity: O(n) + O (k * n), time it takes to find the k-most frequent items  = O(n)
    # Space Complexity: O(n)
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numCount = {}
        results = []

        for _, value in enumerate(nums):
            numCount[value] = 1 + numCount.get(value, 0)

        for i in range(0, k):
            maxKey = max(numCount, key=numCount.get)
            results.append(maxKey)
            numCount.pop(maxKey)
        return results

    # Time Complexity: O(k * log n), removal from heap takes log(n)
    # time and this has to be done k number of times to get the k-most frequent elems.
    # Note: Creating a heap from a list is a O(n) operation
    # Space Complexity: O(n), where n is the length of the nums array: in the worst case,
    #   each array elem is distinct heap and nums have the same size
    def topKFrequentHeapMethod(self, nums, k):
        numCount = {}
        results = []
        for _, value in enumerate(nums):
            numCount[value] = numCount.get(value, 0) + 1

        items = [(-value, key) for key, value in numCount.items()]
        heapq.heapify(items)

        for i in range(0, k):
            results.append(heapq.heappop(items)[1])
        return results

    # Time Complexity: O(n) - Linear time to build hashmap/fill buckets arr, linear time to iterate through buckets at the end
    # Space Complexity: O(n) size of hashmap and buckets array depend on the size of the input arr

    def topKFrequentBucketSortMethod(self, nums, k):
        numCount = {}
        results = []
        buckets = [[] for _ in range(len(nums) + 1)]

        # Count the frequency of each number in the array
        for _, value in enumerate(nums):
            numCount[value] = numCount.get(value, 0) + 1

        # Store hashmap value into array based on how many times they occur in the original nums array
        for newKey, val in numCount.items():
            buckets[val].append(newKey)

        # Starting from the end of the buckets arr (bucket representing the most of amount of times number can appear in list)\
        # add numbers from buckets until results array has k elements+
        for i in range(len(buckets) - 1, -1, -1):
            for elem in buckets[i]:
                results.append(elem)
                if len(results) == k:
                    return results
        return results


if __name__ == "__main__":
    s = Solution()
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    print(s.topKFrequentHeapMethod(nums, 2))
