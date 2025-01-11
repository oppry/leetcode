# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def takeSecond(elem):
    return elem[1]

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        while(list1 != None):
            s.append([list1, list1.val])
            list1 = list1.next
        while(list2 != None):
            s.append([list2, list2.val])
            list2 = list2.next
        s.sort(key=takeSecond, reverse=True)
        prev = None
        for i in s:
            #print(i,prev)
            i[0].next = prev
            prev=i[0]

        return prev
    