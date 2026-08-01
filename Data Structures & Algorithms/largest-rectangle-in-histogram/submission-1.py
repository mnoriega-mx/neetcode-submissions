class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rectangle = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][-1]:
                j, h = stack.pop()
                w = i - j
                area = w * h
                max_rectangle = max(area, max_rectangle)
                start = j
            stack.append((start, height))
        
        while stack:
            i, h = stack.pop()
            w = len(heights) - i
            area = w * h
            max_rectangle = max(area, max_rectangle)
        
        return max_rectangle