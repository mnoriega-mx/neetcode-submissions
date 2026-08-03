class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        partition = l

        if partition != 0 and target >= nums[0] and target <= nums[partition - 1]:
            l, r = 0, partition - 1
        else:
            l, r = partition, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1