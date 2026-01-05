// #203 - Remove Linked List Elements
// Problem solved by Adity
// Time Complexity: O(n) - Each node is visited once through recursive calls.
// Space Complexity: O(n) - Due to the recursion stack for n nodes.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        // Base case: if we've reached the end of the list
        if (head == null) return null;

        // Recur on the rest of the list
        head.next = removeElements(head.next, val);

        // If current node matches val, skip it
        if (head.val == val) {
            return head.next;
        } else {
            return head;
        }
    }
}


----------------------------------------------------------------------------------
APPROACH 2
----------------------------------------------------------------------------------

// #203 - Remove Linked List Elements
// Problem solved by Adity
// Time Complexity: O(n) - Each node is visited once.
// Space Complexity: O(1) - No extra space used beyond a few pointers.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        // Create a dummy node before head to handle edge cases cleanly
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        // Pointer to traverse the list
        ListNode current = dummy;

        // Iterate through the list
        while (current.next != null) {
            if (current.next.val == val) {
                // Skip the node with the target value
                current.next = current.next.next;
            } else {
                // Move forward
                current = current.next;
            }
        }

        // Return the new head (dummy.next)
        return dummy.next;
    }
}
