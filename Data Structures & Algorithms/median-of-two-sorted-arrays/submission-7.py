class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            short = nums1
            long = nums2
        else:
            short = nums2
            long = nums1

        total_length = len(short) + len(long)
        half = total_length // 2

        l, r = 0, len(short)
        while l <= r:
            k = l + (r - l) // 2

            left_s = float('-inf') if k == 0 else short[:k][-1]
            right_s = float('inf') if k == len(short) else short[k:][0]

            partition = half - k

            left_l = float('-inf') if partition == 0 else long[:partition][-1]
            right_l = float('inf') if partition == len(long) else long[partition:][0]

            if left_s <= right_l and left_l <= right_s:
                if total_length % 2 == 0:
                    return (min(right_s, right_l) + max(left_s, left_l)) / 2
                return min(right_s, right_l)
            
            if left_s > right_l:
                r = k - 1
            else:
                l = k + 1