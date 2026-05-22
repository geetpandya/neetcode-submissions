class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        streak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                streak += 1
                
            if max_streak < streak:
                max_streak = streak

            elif nums[i] == 0:
                streak = 0
        
        return max_streak