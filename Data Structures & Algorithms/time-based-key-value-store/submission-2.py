class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = ''

        for k in self.time_map:
            if k == key:
                for i in range(len(self.time_map[k]) - 1, -1, -1):
                    if self.time_map[k][i][1] <= timestamp:
                        res = self.time_map[k][i][0]
                        break
        return res

        