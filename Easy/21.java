/**
 * #21 - Merge Two Sorted Lists
 * Problem solved by Adity
 * 
 * Time Complexity: O(n) - We iterate through both lists once, where n is the total number of nodes in both lists.
 * Space Complexity: O(1) - Constant space used, only pointers for traversing the lists.
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Pointers to traverse both input lists
        ListNode head = list1;
        ListNode head2 = list2;

        // Dummy node to simplify list building, result will start from this node's next
        ListNode resultList = new ListNode();
        ListNode result = resultList;

        // Traverse both lists and merge them in sorted order
        while (head != null && head2 != null) {
            // If the value of list1 node is greater, take the node from list2
            if (head.val > head2.val) {
                result.next = head2;
                head2 = head2.next; // Move to the next node in list2
            } else {
                result.next = head;
                head = head.next; // Move to the next node in list1
            }
            result = result.next; // Move the result pointer forward
        }

        // If one of the lists is exhausted, attach the remaining part of the other list
        if (head != null) result.next = head;
        if (head2 != null) result.next = head2;

        // Return the merged list, skipping the dummy node
        return resultList.next;
    }
}
