class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ansdic = {}
        start = 0
        maxlen = 0
        for end in range(len(s)):
            if s[end] in ansdic:
                start = max(start,ansdic[s[end]]+1)
            ansdic[s[end]] = end
            maxlen = max(maxlen, end - start +1)
        return maxlen
        