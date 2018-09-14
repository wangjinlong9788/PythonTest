        

#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
"""def sortedInsert(head, data):
    dhead=head
    position=0
    while(dhead.data):
        if dhead.data<data:
            position+=1
        dhead=dhead.next
            #if dhead.data>data:
    dhead=head
    for i in range(position):
        dhead=dhead.next
        
    insert=DoublyLinkedListNode(data)
    #
    insert.next=dhead.next
    #dhead.next.prev=insert
    dhead.next=insert
    insert.prev=dhead
    return head

 
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 """
 
class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

# return the head node of the updated list 
 
def sortedInsert(head, data):
    if head is None:
        return Node(data)
    elif data < head.data:
        n = Node(data, head)
        head.prev = n
        return n
    else:
        ptr = head
        while ptr.next and ptr.next.data < data: ptr = ptr.next
        n = Node(data, ptr.next, ptr)
        if ptr.next: ptr.next.prev = n
        ptr.next = n
        return head




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
