class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
#生命周期 __new__  ->  __init__  -> __del__
'''
if __name__ == '__main__':
    # l1 = ListNode(1)    
    # l2 = ListNode(2)
    # l3 = ListNode(3)

    # l1.next = l2
    # l2.next = l3

    # #单链表遍历
    # while l1 != None:
    #     print(l1.val)
    #     l1 = l1.next

    #尾插法
    #根据数组创建单链表的方法
    ary = [1,2,3]
    prehead = ListNode(-1)
    prev = prehead

    #头插法
    for i in range(len(ary)):
        curval = ary[i]
        li = ListNode(curval)
        prev.next = li
        prev = prev.next
    return prehead.next
'''

class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        #prev.next = l1 if l1 is not None else l2

        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2

        return prehead.next

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

                    

