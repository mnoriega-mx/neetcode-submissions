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
        print(short, long)
        while l <= r:
            k = l + (r - l) // 2
            print(k)

            if k == 0:
                left_s = float('-inf')
            else:
                left_s = short[:k][-1]

            if k == len(short):
                right_s = float('inf')
            else:
                right_s = short[k:][0]

            partition = half - k
            print(half, '-', k, '=', partition)
            
            if partition == 0:
                left_l = float('-inf')
            else:
                left_l = long[:partition][-1]
            
            if partition == len(long):
                right_l = float('inf')
            else:
                right_l = long[partition:][0]

            print(left_s, right_s, '', left_l, right_l)

            print(left_s, '<=' ,right_l, left_l, '<=' ,right_s)
            if left_s <= right_l and left_l <= right_s:
                if total_length % 2 == 0:
                    return (min(right_s, right_l) + max(left_s, left_l)) / 2
                return min(right_s, right_l)
            
            if left_s > right_l:
                r = k - 1
            else:
                l = k + 1