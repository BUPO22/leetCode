class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s
        
        result =[""] * numRows
        index =0
        added = 1

        for char in s:
            result[index] += char
            if index == numRows-1: added = -1
            if index == 0: added = 1
            index += added
        
        return "".join(result)
