# This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson.

# Given a pointer to the head of a singly-linked list, print each  value from the reversed list. If the given list is empty, do not print anything.

# Example

#  refers to the linked list with  values 

# Print the following:
# 3
# 2
# 1

# Function Description

# Complete the reversePrint function in the editor below.

# reversePrint has the following parameters:

# SinglyLinkedListNode pointer head: a reference to the head of the list
# Prints

# The  values of each node in the reversed list.

# Input Format

# The first line of input contains , the number of test cases.

# The input of each test case is as follows:

# The first line contains an integer , the number of elements in the list.
# Each of the next n lines contains a data element for a list node.
# Constraints

# , where  is the  element in the list.
# Sample Input

# 3
# 5
# 16
# 12
# 4
# 2
# 5
# 3
# 7
# 3
# 9
# 5
# 5
# 1
# 18
# 3
# 13
# Sample Output

# 5
# 2
# 4
# 12
# 16
# 9
# 3
# 7
# 13
# 3#!/bin/python3

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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):

    if head == None:
        pass
    else:
        if head.next == None:
            print(head.data)
        else:
            reversePrint(head.next)
            print(head.data)
if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)

# 18
# 1
# 5
# Explanation

# There are three test cases. There are no blank lines between test case output.

# The first linked list has  elements: . Printing this in reverse order produces:
# 5
# 2
# 4
# 12
# 16

# The second linked list has  elements: . Printing this in reverse order produces:
# 9
# 3
# 7
# The third linked list has  elements: . Printing this in reverse order produces:
# 13
# 3
# 18
# 1
# 5



