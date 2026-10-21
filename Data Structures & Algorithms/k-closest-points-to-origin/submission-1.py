import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x, y in points:

            heapq.heappush(heap, (-(x * x + y * y), [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for item in heap:
            distance = item[0]
            point = item[1]
            result.append(point)

        return result