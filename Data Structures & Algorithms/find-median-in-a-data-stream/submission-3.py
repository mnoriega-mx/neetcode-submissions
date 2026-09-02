class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        if not self.stream:
            self.stream.append(num)
            return
        if num >= self.stream[-1]:
            self.stream.append(num)
            return
        if num <= self.stream[0]:
            self.stream.insert(0, num)
            return

        l, r = 0, len(self.stream) - 1

        mid = l + (r - l) // 2
        while l < r:
            mid = l + (r - l) // 2

            if self.stream[mid] == num:
                self.stream.insert(mid, num)
                return
            if self.stream[mid] < num:
                l = mid + 1
            else:
                r = mid
        
        if self.stream[mid] >= num:
            self.stream.insert(mid, num)
        else:
            self.stream.insert(mid+1, num)

    def findMedian(self) -> float:
        length = len(self.stream)
        mid = length // 2 - 1

        if length == 1:
            return self.stream[0]
        
        if length % 2 == 0:
            median = (self.stream[mid] + self.stream[mid+1]) / 2
        else:
            median = self.stream[mid+1]
        
        return median