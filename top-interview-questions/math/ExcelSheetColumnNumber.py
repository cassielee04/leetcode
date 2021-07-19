class Solution171:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(0,len(columnTitle)):
            res = res * 26
            res += ord(columnTitle[i]) - ord("A") +1 
            
        return res