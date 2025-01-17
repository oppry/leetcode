# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def solution0(head, val):
    cur = head
    while cur != None and cur.val == val:
        head = cur.next
        cur = head
    prev = cur
    #print("1 - ", cur.val, head.val)
    while cur != None:
        if cur.val == val:
            cur = cur.next
            prev.next = cur
            #print("2 - ", prev.val, cur.val)
        else:
            prev = cur
            cur = cur.next
            #print("3 - ", prev.val, cur.val)
    return head

def solution1(head, val):
    if head == None:
        return head
    head.next = solution1(head.next, val)
    return head if head.val != val else head.next

def solution2(head, val):
    dumpHead = ListNode(0, head)
    cur = dumpHead
    while cur.next != None:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dumpHead.next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        return solution2(head, val)
    