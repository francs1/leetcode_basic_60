class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: 'ListNode') -> bool:        
        lists = []
        while head != None:
            lists.append(head.val)
            head = head.next
        i,j = 0,len(lists)-1
        while i < j:
            if lists[i] != lists[j]:
                return False
            i += 1
            j -= 1
        return True