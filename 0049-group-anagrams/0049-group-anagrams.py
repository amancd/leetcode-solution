class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)

        for st in strs:

            sorted_words = "".join(sorted(st))

            ans[sorted_words].append(st)
        
        return list(ans.values())