class Solution118:
    def generate(self, numRows: int) -> List[List[int]]:
        start = 1
        res = []
        next_arr = []
        res.append([1])
        
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        for i in range(1, numRows): 
            next_arr.append(1)
            for j in range(1,i): 
                next_arr.append(res[i-1][j-1] + res[i-1][j])
                
            next_arr.append(1)
            res.append(next_arr)
            next_arr = []
            
        return res
                