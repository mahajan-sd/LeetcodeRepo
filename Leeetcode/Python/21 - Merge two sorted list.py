# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
            
        
#==============================================================================
# Another approach with list, simple and easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        temp = []
        while curr :
            temp.append(curr.val)
            curr = curr.next
        curr = list2
        while curr :
            temp.append(curr.val)
            curr = curr.next
        temp.sort()
        print(temp)
        if  len(temp)>0:
            dummy = ListNode(temp[0])
            head = dummy
            for i in temp[1:]:
                head.next = ListNode(i)
                head = head.next
            return dummy
        return ListNode('')

        
