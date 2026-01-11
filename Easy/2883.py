# #2883 - Drop Missing Data
# Problem solved by Adity
# Time Complexity: O(n) - pandas scans rows for missing values
# Space Complexity: O(1) - no extra space beyond result DataFrame

import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
