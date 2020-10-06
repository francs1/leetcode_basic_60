class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getIntersectionNode(self, headA: 'ListNode', headB: 'ListNode') -> ListNode:
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempA = headA
        tempB = headB
        while tempA != tempB:
            if tempA == None:
                tempA = headB
            else:
                tempA = tempA.next
            if tempB == None:
                tempB = headA
            else:
                tempB = tempB.next
        return tempA