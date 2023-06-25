class Solution(object):
    # 
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        result = 0
        l = 0
        for r in range(len(s)):
            # Increment count of char in hash table
            count[s[r]] = 1 + count.get(s[r], 0)

            # While the length of the subsrtring minus value of most frequent char in subString is greater,
            # than the number of replacements allowed, slide window to the right (move left pointer)
            while (r - l + 1) - max(count.values()) > k:
                # decrement count of char at left pointer
                count[s[l]] -= 1
                l += 1
            # Update result if length of substring is greater
            result = max(result, r - l + 1)
        return result


if __name__ == "__main__":
    s = Solution()
    testStr = "AABABBA"
    k = 1
    print(s.characterReplacement(testStr, k))
