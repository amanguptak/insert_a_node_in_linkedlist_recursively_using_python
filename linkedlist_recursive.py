# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:43:06 2021

@author: Aman gupta
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next

            newnode = Node(data)
            temp.next = newnode

    def printl(self):
        currentNode = self.head
        while (currentNode != None):
            print(currentNode.data)
            currentNode = currentNode.next

def inserk(head, i, data):

        if i == 1:
            newnode = Node(data)
            newnode.next=head

            return  newnode
        else:
            asd = inserk(head.next,i - 1, data)
            head.next = asd
            return head


l1 = linkedlist()
l = [1, 2, 3, 4, 6]

for i in l:
    l1.insert(i)
l1.printl()
print()
inserk(l1.head,4,9)
inserk(l1.head,7,10)
print("this part is recursevly added")


l1.printl()
