class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1, len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:
                    output.append(count)
                    break
            else:
                output.append(0)
            

        return output