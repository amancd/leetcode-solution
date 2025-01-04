class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        def fn(string):
            char_indices = {}
            duplicates = {}

            for i, char in enumerate(string):
                if char in char_indices:
                    if char not in duplicates:
                        duplicates[char] = [char_indices[char]]
                    duplicates[char].append(i)
                else:
                    char_indices[char] = i

            return duplicates
        
        res = fn(s)

        def fn2(l, r):
            return len(set(s[l+1:r]))


        count = 0
        for k, v in res.items():
           left = v[0]
           right = v[-1]
           count += fn2(left, right)
           
        
        if not res:
            return 0

        return count