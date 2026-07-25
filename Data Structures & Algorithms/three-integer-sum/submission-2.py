class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                add = nums[i] + nums[j] + nums[k]
                if add == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    j += 1
                elif add < 0:
                    j += 1
                else:
                    k -= 1
        
        return triplets