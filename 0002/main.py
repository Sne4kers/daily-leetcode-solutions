# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return l2
        if l2 == None:
            return l1
        if l1 == None:
            return l2
        
        head_l3 = None
        current_l3= None
        overflow = 0
        while l1 != None and l2 != None:
            if head_l3 == None:
                head_l3 = ListNode(val=(l1.val + l2.val + overflow) % 10, next=None)
                current_l3 = head_l3
                overflow = (l1.val + l2.val + overflow) // 10
            else:
                new_node = ListNode(val=(l1.val + l2.val + overflow) % 10, next=None)
                overflow = (l1.val + l2.val + overflow) // 10
                current_l3.next = new_node
                current_l3 = current_l3.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            new_node = ListNode(val=(l1.val + overflow) % 10, next=None)
            overflow = (l1.val + overflow) // 10
            current_l3.next = new_node
            current_l3 = current_l3.next
            l1 = l1.next
        
        while l2 != None:
            new_node = ListNode(val=(l2.val + overflow) % 10, next=None)
            overflow = (l2.val + overflow) // 10
            current_l3.next = new_node
            current_l3 = current_l3.next
            l2 = l2.next
        
        if overflow != 0:
            new_node = ListNode(val=overflow, next=None)
            current_l3.next = new_node
        
        return head_l3
        
