class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequencies = {}

        for i in nums:
            frequencies[i] = frequencies.get(i, 0) + 1
        
        bucket = [[] for i in range(len(nums))]

        for n, f in frequencies.items():
            for i in range(f):
                bucket[f - 1].append(n)
        
        output = []
        for frequency in bucket:
            frequency.sort(reverse=True)
            for num in frequency:
                output.append(num)
        
        return output