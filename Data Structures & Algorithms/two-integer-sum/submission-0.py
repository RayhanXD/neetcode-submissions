class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        new_hash = {}

        for i, num in enumerate(nums):
            if (target - num) in new_hash:
                return [new_hash[target - num], i]
            else:
                new_hash[num] = i

        return []
        