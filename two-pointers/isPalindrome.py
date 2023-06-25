class Solution(object):
    # Time-complexity: O(n), in the worst-case (str is a palindrome), pointers meet in the middle of the string, only traverses through once
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Lowercase the string and remove all non-alphanumeric characters
        s = "".join(c for c in s.lower() if c.isalnum())

        if (len(s) == 0):
            return True
        else:
            # Use two pointers, if character at both pointers isn't the same,\
            # str is not a palindrome
            l = 0
            r = len(s) - 1
            while (l < r):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True


if __name__ == "__main__":
    sol = Solution()
    str = "aa"
    print(sol.isPalindrome(str))
