# Problem: Linked List Cycle


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Looks for cycle in by storing previously seen nodes in a set
# Runtime: O(n)
# Memory: O(n)
def hasCycleUsingSetImplementation(head):
    seenNodes = set()
    if head is None:
        return False
    while head is not None:
        if head in seenNodes:
            return True
        seenNodes.add(head)
        head = head.next
    return False


# Looks for cycle using fast and slow pointer (Sliding window)
# Runtime: O(n)
# Memory: O(1)
def hasCycleUsingSlidingWindow(head):

    if head is None:
        return False

    pointerA = head  # slow pointer
    pointerB = head.next  # fast pointer

    while pointerA.val != pointerB.val:
        # If you reach the end of the list without finding cycle, return false
        if pointerB is None or pointerB.next is None:
            return False
        pointerA = pointerA.next
        pointerB = pointerB.next.next
    return True


if __name__ == "__main__":
    print("Hello World!")
