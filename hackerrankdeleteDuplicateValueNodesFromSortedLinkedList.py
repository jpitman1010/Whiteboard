# This challenge is part of a tutorial track by MyCodeSchool

# You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete nodes and return a sorted list with each distinct value in the original list. The given head pointer may be null indicating that the list is empty.

# Example

#  refers to the first node in the list .

# Remove 1 of the  data values and return  pointing to the revised list .

# Function Description

# Complete the removeDuplicates function in the editor below.

# removeDuplicates has the following parameter:

# SinglyLinkedListNode pointer head: a reference to the head of the list
# Returns

# SinglyLinkedListNode pointer: a reference to the head of the revised list
# Input Format

# The first line contains an integer , the number of test cases.

# The format for each test case is as follows:

# The first line contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the  value for each of the elements of the linked list.

# Constraints

# Sample Input

# 1
# 5
# 1
# 2
# 2
# 3
# 4
# Sample Output

# 1 2 3 4 
# Explanation

# The initial linked list is: .

# The final linked list is: .


#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    
    #while current.next != none:
    #current = head
    #traverse the llist and check if current.next.data == current.data
    #if yes: current.next == current.next.next
    #current = current.next
    #if current.next == none:
    #return head

    current = head.next
    prev = head
    
    while current != None:
        print('while current.next != None, prev =', prev.data)
        print('while current.next != None, current =', current.data)
        if current.data == prev.data:
            prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next
    return head
    
    
    
if __name__ == '__main__':