# Problem: Longest SubString (Solved using sliding window technique)
# Runtime: O(n)
# Memory : O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i, j = 0, 0
        # Use hashset to keep track of seen chars
        seenChars = set()
        maxLength = 0
        while (j < len(s)):
            if s[j] not in seenChars:
                seenChars.add(s[j])
                j += 1
            else:
                maxLength = max(maxLength, len(seenChars))
                seenChars.remove(s[i])
                i += 1
        return max(maxLength, len(seenChars))

    def lengthOfLongestSubstringAlternate(self, s):
        charSet = set()
        l = 0
        result = 0
        for r in range(len(s)):
            # Remove all duplicates from charSet
            while s[r] in charSet:
                charSet.remove(s[l])
                # As you remove duplicate, slide window to the right
                l += 1
            charSet.add(s[r])
            result = max(result, len(charSet))
        return result


if __name__ == "__main__":
    str = "pwwkew"
    s = Solution()
    print(s.lengthOfLongestSubstringAlternate(str))
