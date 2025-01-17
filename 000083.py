# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #print(set1)
        bianli = head
        while(bianli != None and bianli.next != None):
            if(bianli.val == bianli.next.val):
                bianli.next = bianli.next.next
            else:
                bianli = bianli.next
        if(bianli != None):
            bianli.next = None
        return head
