# #326 - Power of Three
# Problem solved by Adity
# Time Complexity: O(1) - Logarithm calculation takes constant time.
# Space Complexity: O(1) - No extra space used apart from variables.

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        diff = round(math.log(n, 3)) - math.log(n, 3)
        
        if abs(diff) < 1e-10:
            return True
        else:
            return False