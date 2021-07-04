class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution141HashSet:
    def hasCycle(self, head: ListNode):
        my_set = set()
        while head:
            if head not in my_set:
                my_set.add(head)
            else:
                return True
            head = head.next
        
        return False

class Solution141FastSlowPointers:
        def hasCycle(self, head: ListNode) -> bool:
            if head is None:
                return None
            
            slow = head
            fast = head.next
            
            while fast and fast.next:
                if slow == fast:
                    return True
                
                slow = slow.next
                fast = fast.next.next
            
            return False
            