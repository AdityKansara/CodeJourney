# #1779 - Find Closest Number to Target
# Problem solved by Adity
# Time Complexity: O(1) - Constant time distance comparison
# Space Complexity: O(1) - No extra space used


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Calculate distances from z
        dist_x = abs(x - z)
        dist_y = abs(y - z)

        # Compare distances and return result
        if dist_x < dist_y:
            return 1
        elif dist_x > dist_y:
            return 2
        else:
            return 0
