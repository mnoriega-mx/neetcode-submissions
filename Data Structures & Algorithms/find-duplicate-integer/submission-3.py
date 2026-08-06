class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while True:
            if slow == fast:
                break
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while True:
            if slow == slow2:
                return slow
            slow = nums[slow]
            slow2 = nums[slow2]