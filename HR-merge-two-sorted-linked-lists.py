
# PRACTICE
# CERTIFICATION
# COMPETE
# CAREER FAIR
# Expand
# Search
# jpitman1010
# PracticeData StructuresLinked ListsMerge two sorted linked lists
# Merge two sorted linked lists

# 1330.7 more points to get your next star!
# Rank: 144055|Points: 869.3/2200
# Problem Solving
# Your Merge two sorted linked lists submission got 5.00 points.  
# You are now 1330.7 points away from the 6th star for your problem solving badge.
# Try the next challenge | Try a Random Challenge
# Problem
# Submissions
# Leaderboard
# Discussions
# Editorial
# This challenge is part of a tutorial track by MyCodeSchool

# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

# Example
#  refers to 
#  refers to 

# The new list is 

# Function Description

# Complete the mergeLists function in the editor below.

# mergeLists has the following parameters:

# SinglyLinkedListNode pointer headA: a reference to the head of a list
# SinglyLinkedListNode pointer headB: a reference to the head of a list
# Returns

# SinglyLinkedListNode pointer: a reference to the head of the merged list
# Input Format

# The first line contains an integer , the number of test cases.

# The format for each test case is as follows:

# The first line contains an integer , the length of the first linked list.
# The next  lines contain an integer each, the elements of the linked list.
# The next line contains an integer , the length of the second linked list.
# The next  lines contain an integer each, the elements of the second linked list.

# Constraints

# , where  is the  element of the list.
# Sample Input

# 1
# 3
# 1
# 2
# 3
# 2
# 3
# 4
# Sample Output

# 1 2 3 3 4 
# Explanation

# The first linked list is: 

# The second linked list is: 

# Hence, the merged linked list is: 

# Python 3



# 505152535455565758596061626364656766494546474842434439404132333435363738293031
#                 merged.insert_node(head2.data)
#                 head2 = head2.next
#                 head1 = head1.next
#     return merged.head
    
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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    
    # make new llist to combine both head1 and head2 sorted
    #look first node from each list, smallest is added to new llist
    # increment forward smaller node to node.next
    #  if nodeA and nodeB are ==, add both and increment forward both lists
    # compare new node to current node on larger node list, repeat above
    # if node == None: add the rest of the other linked list
    
    
    merged = SinglyLinkedList()
    
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    else:
        while head1 or head2:
            if head1 == None and head2.data != None:
                merged.insert_node(head2.data)
                head2 = head2.next
            elif head2 == None and head1.data != None:
                merged.insert_node(head1.data)
                head1 = head1.next    
            elif head1.data > head2.data:
                merged.insert_node(head2.data)
                head2 = head2.next
            elif head2.data > head1.data:
                merged.insert_node(head1.data)
                head1 = head1.next
            else:
                merged.insert_node(head1.data)
                merged.insert_node(head2.data)
                head2 = head2.next
                head1 = head1.next
    return merged.head
    
    

if __name__ == '__main__':   


    Line: 82 Col: 35
    Submit CodeRun Code
    Upload Code as File
    Test against custom input
    Problem Solving
    You have earned 5.00 points!
    You are now 1330.7 points away from the 6th star for your problem solving badge.
    1%869.3/2200
    Congratulations
    Share on FacebookShare on TwitterShare on LinkedIn
    You solved this challenge. Would you like to challenge your friends?
    Next Challenge
    Earn a certificate in Problem Solving
    Kudos on your progress! Take the HackerRank Skills Certification test and enrich your profile

