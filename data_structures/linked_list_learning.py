from operator import itruediv
from pdb import post_mortem


class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next = next
    

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    ### to test insert at beginning func, 
    ### add a print function
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data) + '-->'
                itr = itr.next
            print(llstr)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            

            itr.next = Node(data, None)

    ### create a linkedlist from new list

    def insert_values(self, data_list):
        ### wipe out all the nodes
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    ### get the length of the linkedlist
    def get_length(self):
        cnt = 0
        itr = self.head
        while itr:
            cnt +=1
            itr = itr.next

        return cnt

    ### removed the node at a poistion

    def remove_at(self, position):
        if position < 0 or position > self.get_length():
            raise Exception("Invalid Index Position ")
        
        if position == 0:
            self.head = self.head.next
            return
        cnt = 0
        itr = self.head

        while itr:
            if cnt == position - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            cnt +=1

    ### insert node at a position
    def insert_at(self, position, data):
        if position < 0 or position  > self. get_length():
            raise Exception("Invalid position")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        cnt = 0
        itr = self.head

        while itr:
            if cnt == position -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            cnt += 1






if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['banana','mango','grapes', 'orange'])
    print('Length of the Linked List', ll.get_length())
    ll.print()
    ll.insert_at(0, "FIGS")
    ll.print()
    ll.insert_at(0, "JACKFRUIT")
    ll.print()
    
