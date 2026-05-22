class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = 2 * n * [0]
        for i in range(len(nums)):
            ans[i] = ans[n+i] = nums[i]

        return ans 