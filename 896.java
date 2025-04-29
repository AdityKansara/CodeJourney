// #896 - Monotonic Array
// Problem solved by Adity
// Time Complexity: O(n) - Loop through the array once
// Space Complexity: O(1) - Constant space used

class Solution {
    public boolean isMonotonic(int[] nums) {
        // Initialize two flags to check if the array is monotonically increasing or decreasing
        boolean isMonoI = true;
        boolean isMonoD = true;

        // Loop through the array to check for both increasing and decreasing conditions
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                isMonoI = false;  // Not increasing
            } else if (nums[i] > nums[i + 1]) {
                isMonoD = false;  // Not decreasing
            }
        }

        // Return true if the array is either monotonically increasing or decreasing
        return isMonoI || isMonoD ;
    }
}
