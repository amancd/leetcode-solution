class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)

        for st in strs:

            sorted_words = "".join(sorted(st))

            print(sorted_words)

            ans[sorted_words].append(st)
        
        return list(ans.values())