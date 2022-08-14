# Problem: Longest SubString (Solved using sliding window technique)
# Runtime: O(n)
# Memory : O(n)
def lengthOfLongestSubString(s):
    i = 0  # Left corner of sliding window
    j = 0  # Right corner of sliding window
    seenChars = set()
    maxLength = 0
    for char in s:
        # If char isn't in set,
        # Increase the sliding window from the right
        if char not in seenChars:
            seenChars.add(s)
            j = j + 1
        else:
            # If character is in set, increase
            # the sliding window from the left (remove character currently at left pointer)
            seenChars.remove(char)
            i = i + 1
            maxLength = max(len(seenChars), maxLength)
    return maxLength


if __name__ == "__main__":
    print("Hello World")
