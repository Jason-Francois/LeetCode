class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # Create freq table for s1
        s1Count = {}
        for c in s1:
            s1Count[c] = 1 + s1Count.get(c, 0)

        l, r = 0, 0
        seen = {}
        while (r < len(s2)):
            if s2[r] in s1Count:
        return False


if __name__ == "__main__":
    s = Solution()
    s1 = "adc"
    s2 = "dcda"

    print(s.checkInclusion(s1, s2))
