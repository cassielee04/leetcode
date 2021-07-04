class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution234:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        for i in range(0,len(res)//2):
            if res[i] != res[len(res)-i-1]:
                return False
        
        return True

