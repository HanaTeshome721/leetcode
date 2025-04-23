from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        # Iterate over all possible hours (0 to 11) and minutes (0 to 59)
        for h in range(12):  # Hours range from 0 to 11
            for m in range(60):  # Minutes range from 0 to 59
                # Count the number of 1s in the binary representations of hour and minute
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # If the total number of 1s equals the turnedOn value, add to result
                    result.append(f"{h}:{m:02d}")  # Format minutes as two digits
        
        return result
