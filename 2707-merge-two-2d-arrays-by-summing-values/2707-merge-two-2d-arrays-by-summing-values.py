class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        freq = {}
        ans = []

        for a, b in nums1:
            if a not in freq:
                freq[a] = b
        
        for a, b in nums2:
            if a not in freq:
                freq[a] = b
            else:
                freq[a] += b
        

        for k, v in freq.items():
            ans.append([k, v])
        

        ans.sort()

        return ans