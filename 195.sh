# #195 - Print 10th Line
# Problem solved by Adity
# This uses `sed` to print the 10th line of the file.
# Time Complexity: O(n) - It processes the file line by line.
# Space Complexity: O(1) - We only store the pattern.

sed -n '10p' file.txt
