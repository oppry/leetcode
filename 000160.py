# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def solution0(headA, headB):
    cur = headA
    listA, listB= [], []
    while cur != None:
        listA.insert(0, cur)
        cur = cur.next
    cur = headB
    while cur != None:
        listB.insert(0, cur)
        cur = cur.next
    prev = None
    for i in range(0, min(len(listA),len(listB))):
        #print(i, listA[lenA-i].val, listB[lenB-i].val)
        if(listA[i] != listB[i]):
            return prev
        prev = listA[i]
    return prev

def solution1(headA, headB):
    s = set()
    while headA:
        s.add(headA)
        headA = headA.next
    
    while headB:
        if headB in s:
            return headB
        headB = headB.next
    
    return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa
