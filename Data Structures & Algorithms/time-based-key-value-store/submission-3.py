class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = ''

        if key not in self.time_map:
            return res

        pairs = self.time_map[key]
        l, r = 0, len(pairs) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if pairs[mid][1] <= timestamp:
                res = pairs[mid][0]
                l = mid + 1
            else:
                r = mid -1

        return res