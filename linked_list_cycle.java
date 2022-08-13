
//Problem Name: Linked List Cycle
//Difficulty: Easy


/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    
    // NOTE: This is the optimal solution
    // Solution using fast and slow pointers (Floyd's cycle detection algorithm)
    // Memory: O(1)
    // Runtime: O(n)
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        
        ListNode slow = head;
        ListNode fast = head.next;
        
        // Use two pointers, fast and slow
        while(slow != fast){
            if(fast == null || fast.next == null){
                return false; // End of list is reached, no cycle is found
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return true;
    }
    
    
    // Solution using HashSet
    // Memory: O(n)
    // Runtime: O(n)
    public boolean hasCycle(ListNode head){
        HashSet<ListNode> seenNodes = new HashSet<ListNode>();
        if(head == null) return false;
        
        while(head != null){
            if(seenNodes.contains(head)){
                return true;
            }
            seenNodes.add(head);
            head = head.next;
        }
        return false;
    }
}