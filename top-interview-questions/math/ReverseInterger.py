class Solution7:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0

        if x > 0:
            new_num = int(str(x)[::-1])
        
        elif x < 0 :
            new_st = str(x)[1:]
            new_num = -int(str(new_st)[::-1])
        
        if new_num > pow(2, 31) or new_num < pow(-2,31):
            return 0 
    
        else:
            return new_num
        
