
class Solution168:
    
    def __init__(self):
        print("init")
    def majorityElement(self, nums):
        dic = {}
        max_val = 0 
        max_key = 0
        
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        for key,value in dic.items():
            
            if value > max_val:
                max_val = value
                max_key = key
                
        return max_key
                