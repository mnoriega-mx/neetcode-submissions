import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x1, y1 in points:
            x2, y2 = 0, 0
            dis = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            distances.append([dis, [x1,y1]])
        
        heapq.heapify(distances)

        output = []
        for i in range(k):
            output.append(heapq.heappop(distances)[1])
        
        return output