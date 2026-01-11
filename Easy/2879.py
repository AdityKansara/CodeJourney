# #2879 - Display the First Three Rows
# Problem solved by Adity
# Time Complexity: O(1) - constant time (head operation)
# Space Complexity: O(1) - no extra space used

import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
