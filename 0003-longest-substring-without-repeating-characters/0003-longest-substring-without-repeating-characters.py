class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maximum = 0
        left = 0

        for right in range(len(s)):
            if len(set(s[left:right+1])) == len(s[left:right+1]):
                maximum = max(maximum, right - left + 1)
                right += 1
            else:
                left += 1
        
        
        return maximum