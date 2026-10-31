class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) <= 10:
            return []
        
        start = 0
        end = 9
        seen = {}
        ans = []

        while end < len(s):
            if s[start: end +1] in seen and seen[s[start: end +1]] ==1:
                ans.append(s[start: end +1])
                seen[s[start: end +1]] = 2

            if s[start: end +1] not in seen:
                seen[s[start: end +1]] = 1

            end += 1
            start += 1

        return ans



