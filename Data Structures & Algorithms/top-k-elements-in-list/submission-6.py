class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        output = {}

        for num in nums:
            if num in output:
                output[num] += 1
            else:
                output[num] = 1

        target_output = []
        
        for i, num in output.items():
            target_output.append([num, i])

        target_output.sort()

        new_output = []

        while len(new_output) < k:
            new_output.append(target_output.pop()[1])
        
        return new_output