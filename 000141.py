# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def check(head):
    s = set()
    while head:
        c_id = id(head)
        #print(c_id, head.val)
        if c_id in s:
            return True
        else:
            s.add(c_id)
        head = head.next
    return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p, fast_p = head, head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False
