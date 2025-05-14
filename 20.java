// #20 - Valid Parentheses
// Problem solved by Adity
// Time Complexity: O(n) - We iterate through the string once, each character is pushed/popped at most once.
// Space Complexity: O(n) - In the worst case, all characters are opening brackets, stored in the stack.

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        // Stack to store opening brackets
        Stack<Character> adity = new Stack<>();

        // Loop through each character in the string
        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            // Push opening brackets to stack
            if (current == '{' || current == '[' || current == '(') {
                adity.push(current);
            } 
            // If it's a closing bracket
            else if (current == '}' || current == ')' || current == ']') {
                // Check for unmatched closing or incorrect pairing
                if (adity.isEmpty() || !checkClosing(adity.pop(), current)) {
                    return false;
                }
            }
        }

        // If stack is empty, all brackets matched
        return adity.isEmpty();
    }

    // Helper method to match brackets
    public boolean checkClosing(char previous, char current) {
        return (current == '}' && previous == '{') || 
               (current == ')' && previous == '(') ||
               (current == ']' && previous == '[');
    }
}
