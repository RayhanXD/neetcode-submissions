class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        table = {}

        for num in nums:
            table[num] = table.get(num, 0) + 1

        for key in table:
            if table.get(key) > 1:
                return key
