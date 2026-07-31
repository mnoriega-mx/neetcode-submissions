class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        queue = collections.deque()

        for i in range(k):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        output.append(nums[queue[0]])


        i, j = 0, k
        while j < len(nums):
            while queue and nums[j] > nums[queue[-1]]:
                queue.pop()
            queue.append(j)

            if i >= queue[0]:
                queue.popleft()
            
            output.append(nums[queue[0]])

            j += 1
            i += 1

        return output