# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged=currentnode=ListNode(0)
        while list1 and list2:
            if list1.val<list2.val:
                currentnode.next=list1
                list1=list1.next
            else:
                currentnode.next=list2
                list2=list2.next
            currentnode=currentnode.next
        currentnode.next=list1 or list2
        merged=merged.next
        return merged
