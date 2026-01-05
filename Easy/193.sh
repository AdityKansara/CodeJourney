# #193 - Phone Number Validator
# Problem solved by Adity
# This script reads from 'file.txt' and outputs all valid phone numbers that match the required formats.
# It checks if each line in the file matches the patterns: (xxx) xxx-xxxx or xxx-xxx-xxxx
# Time Complexity: O(n) - The `grep` command processes each line in the file once, where n is the number of lines in the file.
# Space Complexity: O(1) - We only use a fixed amount of space to store the pattern and match each line without additional memory usage.

grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt
