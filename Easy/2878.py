# #2878 - Get the Size of a DataFrame
# Problem solved by Adity
# Time Complexity: O(1) - shape lookup is constant time
# Space Complexity: O(1) - constant extra space

import pandas as pd
from typing import List


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
