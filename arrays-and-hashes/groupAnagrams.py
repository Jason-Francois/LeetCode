from collections import defaultdict


class Solution(object):
    # Time complexity: m (total # of all strings), * n (log n), time it takes to sort each string
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramGroups = {}
        for s in strs:
            x = "".join(sorted(s))
            if x not in anagramGroups:
                anagramGroups[x] = [s]
            else:
                anagramGroups[x].append(s)
        return list(anagramGroups.values())

    # Time Complexity: O(m (total # of strings) * n (average length of strings)), OPTIMAL SOLUTION
    # Justification:
    def groupAnagramsSimple(self, strs):
        # Use hashmap to group anagrams
        res = defaultdict(
            list
        )  # mapping charCount to list of Anagrams, returns a default value (list), when non-existent key is accessed
        for s in strs:
            count = [0] * 26  # represents letters from a-z

            # Count the number of times each character appears in string
            for c in s:
                count[
                    ord(c) - ord("a")
                ] += 1  # map char to index between 0 and 25 (letters 'a'-'z')
            res[tuple(count)].append(
                s
            )  # lists can't be used as keys to dicts in Python, so tuples are used instead.
        return res.values()


if __name__ == "__main__":
    strs = ["a", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(list(sol.groupAnagramsSimple(strs)))
