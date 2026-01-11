# #2881 - Create a New Column
# Problem solved by Adity
# Time Complexity: O(n) - vectorized column operation
# Space Complexity: O(1) - no extra space beyond the new column

import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees
