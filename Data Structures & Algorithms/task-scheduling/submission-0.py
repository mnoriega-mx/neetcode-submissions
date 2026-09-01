class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for t in tasks:
            counter[t] = counter.get(t, 0) + 1

        heap = []
        for c in counter.values():
            heap.append(-c)
        heapq.heapify(heap)

        queue = deque()

        time = 0
        while heap or queue:
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt < 0:
                    queue.append((cnt, time + n))

            if queue:
                if queue[0][1] == time:
                    heapq.heappush(heap, queue.popleft()[0])
            
            time += 1

        return time