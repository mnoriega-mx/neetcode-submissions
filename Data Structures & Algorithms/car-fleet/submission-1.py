class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrivals = []
        fleets = []

        for i in range(len(position)):
            car = position[i]
            time = (target - position[i]) / speed[i]
            arrivals.append((car, time))

        arrivals.sort()

        fleets.append(arrivals[-1][1])
        for i in range(len(arrivals)-1, -1, -1):
            if arrivals[i][1] > fleets[-1]:
                fleets.append(arrivals[i][1])

        return len(fleets)