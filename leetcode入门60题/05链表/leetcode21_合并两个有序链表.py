class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #递归方式
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next,l1)
            return l2
            
if __name__ == '__main__':
    l1_1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(4)

    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)

    l2_1.next = l2_2
    l2_2.next = l2_3

    S = Solution()
    S.mergeTwoLists(l1_1,l2_1)
