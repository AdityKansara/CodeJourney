# #2469 - Convert the Temperature
# Problem solved by Adity
# Time Complexity: O(1) - Constant time calculation
# Space Complexity: O(1) - Constant extra space


class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
