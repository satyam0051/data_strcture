class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublyll:
    def __init__(self):
        self.head=None

    def add_beg(self,nd):
        new_node=Node(nd)
        new_node.next=self.head

        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node
    def appendnd(self,nd):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        new_node=Node(nd)
        temp.next=new_node
        new_node.prev=temp

    def insertafter(self,nd,gn):
        temp=self.head
        while temp.next is not None:
            if temp.data==gn:
                break
            temp=temp.next
        new_node=Node(nd)
        new_node.next=temp.next
        temp.next=new_node
        new_node.prev=temp
        if new_node.next:
            new_node.next.prev=new_node
    def del_beg(self):
        if self.head is None:
            print('We can not delete')
            return
        self.head=self.head.next
        self.head.prev=None
    def del_end(self):
        temp=self.head
        while temp.next.next is  not None:
            temp=temp.next
        temp.next=None
    def del_after(self,nd):
        temp=self.head
        while temp.next is not None:
            if temp.next.data==nd:
                break
            temp=temp.next
        temp.next=temp.next.next
        temp.next.prev=temp


    def revprint(self):
        temp=self.head
        while temp is not None:
            lst=temp
            temp=temp.next

        while lst is not None:
            print(lst.data,'-->',end=' ')
            lst=lst.prev



    def printll(self):
        temp=self.head
        while temp:
            print(temp.data,'-->',end=' ')
            temp=temp.next


dll=doublyll()
dll.add_beg(4)
dll.add_beg(1)
dll.add_beg(2)
dll.add_beg(3)
dll.printll()
print( )
dll.revprint()
print( )
dll.del_after(2)
dll.printll()
print( )
dll.revprint()
