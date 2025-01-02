class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        res = []

        def check_vowel(word):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return word[0] in vowels and word[-1] in vowels

        for word in words:
            if check_vowel(word):
                ans.append(1)
            else:
                ans.append(0)
        
        for i in range(1, len(ans)):
            ans[i] = ans[i] + ans[i-1]

        for l, r in queries:
            if l == 0:
                query = ans[r]
            else:
                query = ans[r] - ans[l - 1]
            res.append(query)
        
        return res
