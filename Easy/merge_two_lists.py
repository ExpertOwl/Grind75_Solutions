# -*- coding: utf-8 -*-
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, other):
        if other == None:
            return(False)
        if not self.val == other.val:
            return(False)
        else: 
            return(True and self.next == other.next)
    def __repr__(self):
        return(f"val: {self.val}, next:{self.next}")

        
def mergeTwoLists(list1, list2):
    if list1 == None:
        return(list2)
    if list2 == None:
        return(list1)
    if list1.val >= list2.val:
        list2.next = mergeTwoLists(list1, list2.next)
        return(list2)
    else:
        list1.next = mergeTwoLists(list1.next, list2)
        return(list1)

class TestMergeTwoLists(unittest.TestCase):    
    def test_both_lists_empty(self):
        self.assertEqual(mergeTwoLists(None, None), None)
        
    def test_class_eq(self):
        list1 = ListNode(0, None)
        list2 = ListNode(0, None)
        self.assertEqual(list1, list2)
        
    def test_second_list_empty(self):
        list_1 = ListNode(0, None)
        list_2 = None
        result = mergeTwoLists(list_1, list_2)
        expected = list_1
        self.assertEqual(result, expected)
    
    def test_first_list_empty(self):
        list_1 = None
        list_2 = ListNode(0, None)
        result = mergeTwoLists(list_1, list_2)
        expected = list_2
        self.assertEqual(result, expected)
        
    def test_both_list_items_are_equal(self):
        list1 =  ListNode(0, None)
        list2 =  ListNode(0, None)
        expected = ListNode(0, ListNode(0, None))
        result = mergeTwoLists(list1, list2)
        self.assertEqual(result, expected)
    
    def test_item1_larger(self):
        list1 = ListNode(1, None)
        list2 = ListNode(0, None)
        expected = ListNode(0, ListNode(1, None))
        self.assertEqual(mergeTwoLists(list1, list2), expected)
        
    def test_item2_larger(self):
        list1 = ListNode(0, None)
        list2 = ListNode(1, None)
        expected = ListNode(0, ListNode(1, None))
        self.assertEqual(mergeTwoLists(list1, list2), expected)
        
if __name__ == '__main__':
    runner = unittest.main()
        