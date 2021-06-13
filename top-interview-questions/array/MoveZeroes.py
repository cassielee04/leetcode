class Solution283:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        slow = 0
        
        for fast in range(0,len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        
            if nums[slow] != 0:
                slow += 1
            
               
            