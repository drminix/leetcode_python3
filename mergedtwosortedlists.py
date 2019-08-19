# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted linked lists and return it as a new list"""
        """Computational complexity: O(n+m) where n and m are length of two lists, respectively"""
        """Space compleixty: O(1)"""
        #special case when two of them are empty
        if l1 is None and l2 is None:
            return l1
            
        #(0) create the first node
        if l1 is None: 
            #special case when l1 is empty
            first = l2
            l2 = l2.next
        elif l2 is None:
            #special case when l2 is empty
            first = l1
            l1 = l1.next  
        elif l1.val < l2.val:
            #l1 is smaller. Pop l1
            first = l1
            l1 = l1.next # move to the next one
        else:
            #otherwise, pop l2
            first = l2 
            l2 = l2.next # move to the next one
        
        previous = first
        
        #(1) continue until one of them is null
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                previous.next = l1
                previous = l1
                l1 = l1.next
            else:
                previous.next = l2
                previous = l2
                l2 = l2.next
        
        #(2) exhaust the remaining list
        list_toexhaust = l1
        if l1 is None:
            list_toexhaust = l2
        
        while list_toexhaust is not None:
            previous.next = list_toexhaust
            previous = list_toexhaust
            
            #move to the next one
            list_toexhaust = list_toexhaust.next   
        
        #(3) return the result
        return first
            
            
                