class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        hash_nums = {}
        hash_set = set()

        for i, num in enumerate(nums):
            hash_nums[num] = i

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                if target in hash_nums and hash_nums[target] not in (i, j):
                    triplet = [nums[i], nums[j], target]
                    hash_set.add(tuple(sorted(triplet)))

        final_output = []

        for triplet in hash_set:
            final_output.append(list(triplet))

        return final_output




        

        

        
            
        