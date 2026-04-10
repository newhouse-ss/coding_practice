# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # step1: at beginning, I need to adjust curr.next, so use a nextNode first record curr.next.
        # step2: if there's prev, curr.next = prev, prev = curr
        # step3: connect nextNode onto curr, but this will lose nextNode.next, so first use curr = nextNode.next to track.
        # step4: nextNode.next = prev, prev = nextNode
        # 
        curr = head # since we need to return head, use a curr to make iteration.
        prev = None # I use prev to record the former node.

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        return prev