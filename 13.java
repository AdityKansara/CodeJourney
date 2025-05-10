// #13 - Roman to Integer
// Problem solved by Adity
// Time Complexity: O(n) - We iterate once through the string of length n.
// Space Complexity: O(1) - HashMap uses constant space since there are only 7 Roman numerals.

import java.util.HashMap;

class Solution {
    public int romanToInt(String s) {
        int len = s.length();

        // Create a mapping from Roman numeral characters to integer values
        HashMap<String, Integer> roman = new HashMap<>();
        roman.put("M", 1000);
        roman.put("D", 500);
        roman.put("C", 100);
        roman.put("L", 50);
        roman.put("X", 10);
        roman.put("V", 5);
        roman.put("I", 1);

        int value = 0;  // Final result
        int next = 0;   // Value of the next Roman numeral

        // Loop through each character in the string
        for (int i = 0; i < len; i++) {
            // Get the value of the current Roman numeral
            int current = roman.get(String.valueOf(s.charAt(i)));

            // Check and get the next value only if not at the last character
            if ((i + 1) != len) {
                next = roman.get(String.valueOf(s.charAt(i + 1)));
            } else {
                next = 0;  // Set next to 0 if this is the last character
            }

            // If current is less than next, it should be subtracted
            if (current < next) {
                current = -current;
            }

            // Add the current value (or negative if subtraction rule applies)
            value += current;
        }

        return value; // Return the final computed value
    }
}
