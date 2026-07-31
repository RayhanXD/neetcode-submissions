from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_hash = {}

        for num in nums:
            freq_hash[num] = freq_hash.get(num, 0) + 1

        heap = []

        for element, freq in freq_hash.items():
            heappush(heap, [-freq, element])

        heapq.heapify(heap)

        output = []

        counter = 0
        while counter < k:
            output.append((heappop(heap)[1]))
            counter += 1

        return output


        