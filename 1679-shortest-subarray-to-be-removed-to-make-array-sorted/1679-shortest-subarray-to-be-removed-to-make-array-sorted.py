class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        left = 0
        while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == len(arr) - 1:
            return 0

        right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        
        nums1 = arr[:left+1]
        nums2 = arr[right:]
        
        maximum = max(left + 1, len(arr) - right)  # Either prefix or suffix length

        # Add a two-pointer merge logic
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                # Extend sorted length
                maximum = max(maximum, i + 1 + len(nums2) - j)
                i += 1
            else:
                j += 1

        # Return the length of the array minus the maximum sorted length
        return len(arr) - maximum