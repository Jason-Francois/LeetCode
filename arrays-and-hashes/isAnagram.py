class Solution(object):
    # Time Complexity: O(S + T) - need to iterate through both strings
    # Space Complexity: O(S + )
    def isAnagram(self, s, t):
        freqTableA = {}

        for char in s:
            if char not in freqTableA:
                freqTableA[char] = 1
            else:
                freqTableA[char] += 1
        for char in t:
            if char not in freqTableA:
                return False
            else:
                freqTableA[char] -= 1

        for _, val in freqTableA.items():
            if val != 0:
                return False
        return True

    # Time Complexity: O(S)
    # Space Complexity: O(n)
    def isAnagramAlternateSolution(self, s, t):
        countS, countT = {}

        # Length of anagram is equal to length of original string
        if len(s) != len(t):
            return False

        # Make hash table for frequency of chars in each string, then
        # check if hash tables are equal
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(
                s[i], 0
            )  # Use get function to handle case where key doesn't exist
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    # Less efficient because the best sort algorithms only have a (n log n) runtime
    def isAnagramSortedSolution(self, s, t):
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    s1 = "ratwe"
    s2 = "art"
    solution = Solution()
    print(solution.isAnagram(s1, s2))
