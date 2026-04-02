# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedListHead: ListNode = ListNode()
        mergedListPointer = mergedListHead

        while list1 and list2:
            if list1.val > list2.val:
                mergedListPointer.next = list2
                list2 = list2.next
            else:
                mergedListPointer.next = list1
                list1 = list1.next

            mergedListPointer = mergedListPointer.next

        if list1:
            mergedListPointer.next = list1

        if list2:
            mergedListPointer.next = list2
            
        
        return mergedListHead.next