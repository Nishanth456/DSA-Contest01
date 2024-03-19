class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        maxlength = 0
        charindex = {}
        start = 0
        
        for end in range(len(s)):
            if s[end] in charindex and charindex[s[end]] >= start:
                start = charindex[s[end]] + 1
            
            charindex[s[end]] = end
            maxlength = max(maxlength, end - start + 1)
        
        return maxlength