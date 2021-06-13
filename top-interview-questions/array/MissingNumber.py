class Solution268:
    def missingNumber(self, nums) -> int:
        
        #sort first
        nums.sort()
        
        for num in nums:
            next_num = num + 1
            
            if next_num in nums and nums[0] == 0:
                continue
            
            elif nums[0] != 0:
                return 0

            else:
                return num + 1
            
        if len(num) == 1 and num[0] == 1:
            return 0