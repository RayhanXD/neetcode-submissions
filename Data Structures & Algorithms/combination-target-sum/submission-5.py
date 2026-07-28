class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def backtrack(curr, i):
            if sum(curr) == target:
                ans.append(curr[:])
                return
            if sum(curr) > target:
                return
            for j in range(i, len(nums)):
                    curr.append(nums[j])
                    backtrack(curr, j)
                    curr.pop()

        ans = []
        backtrack([], 0)
        return ans
        