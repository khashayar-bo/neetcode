# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        headCopy = head

        count = 0
        while head:
            count += 1
            head = head.next

        head = headCopy

        n = count - n


        for i in range(n):
            if i == n - 1:
                if not head.next:
                    head = None
                    break
                else:
                    head.next = head.next.next
            head = head.next

        if n == 0:
            headCopy = headCopy.next

        return headCopy