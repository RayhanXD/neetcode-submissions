# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        length = 0
        stack_vars = head
        curr = head

        while head is not None:
            length += 1
            head = head.next

        counter = 0
        mid = length // 2
        track_stack = []

        while stack_vars is not None:
            counter += 1
            if counter > mid + 1 and length % 2 != 0:
                track_stack.append(stack_vars)
            elif counter > mid:
                track_stack.append(stack_vars)
            stack_vars = stack_vars.next

        for i in range(mid):
            temp = curr.next
            new_node = track_stack.pop()

            curr.next = new_node
            new_node.next = temp

            curr = temp

        curr.next = None

        



        
        