class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None#前一个节点
        while head != None:
            nextnode = head.next#保存当前节点的next(遍历步骤一)
            head.next = prev#修改head.next指向前一个节点
            prev = head#更新prev为head
            head = nextnode#遍历步骤二
        return prev


'''
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':   
        ary = self.seekList(head)
        #数组反转:方式一
        temp = ary[::-1]
        result = self.createLinkList(temp)
        return result

    #遍历链表存储在list中
    def seekList(self,head):
        temp = []
        while head != None:
            temp.append(head.val)
            head = head.next
        return temp
    
    #头插法创建链表
    def createLinkList(self,ary):        
        prehead = ListNode(-1)
        prev = prehead
        for i in range(len(ary)):
            curval = ary[i]
            li = ListNode(curval)
            prev.next = li
            prev = prev.next
        return prehead.next
'''