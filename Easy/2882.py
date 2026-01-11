# #2882 - Drop Duplicate Rows
# Problem solved by Adity
# Time Complexity: O(n) - pandas scans rows to identify duplicates
# Space Complexity: O(1) - in-place operation, no extra DataFrame created

import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates("email", inplace=True)
    return customers
