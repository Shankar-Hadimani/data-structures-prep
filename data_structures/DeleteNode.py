"""
Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0. The list may be empty after you delete the node. In that case, return a null value.

Example



After removing the node at position , .

Function Description

Complete the deleteNode function in the editor below.

deleteNode has the following parameters:
- SinglyLinkedListNode pointer llist: a reference to the head node in the list
- int position: the position of the node to remove

Returns
- SinglyLinkedListNode pointer: a reference to the head of the modified list

Input Format

The first line of input contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer, the node data values in order.
The last line contains an integer, , the position of the node to delete.

Constraints

, where  is the  element of the linked list.
Sample Input

8
20
6
2
19
7
4
15
9
3
Sample Output

20 6 2 7 4 15 9
Explanation

The original list is . After deleting the node at position , the list is .
"""
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

#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    # create a node
    head = llist
    if position == 0:
        head = head.next
    else:
        temp = head
        cnt = 1
        while temp is not None  and cnt < position:
            temp = temp.next
            cnt +=1
            
        # delete node
        temp.next = temp.next.next
    
    return head
    
        
         
        
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
