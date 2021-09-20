class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class CirLinkedList:

    def __init__(self):
        self.head=None


    def add_beg(self,nd):

        new_node=Node(nd)
        temp=self.head
        new_node.next=self.head

        if self.head is not None:
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
        else:
            new_node.next=new_node

        self.head=new_node
    def spllitlinked(self,head1,head2):
        fast_ptr=self.head
        slow_ptr=self.head

        if self.head is None:
            return
        while (fast_ptr.next!=self.head and fast_ptr.next.next!=self.head):
            fast_ptr=fast_ptr.next.next
            slow_ptr=slow_ptr.next

        if fast_ptr.next.next==self.head:
            fast_ptr=fast_ptr.next
        head1.head=self.head
        if self.head.next!=self.head:
            head2.head=slow_ptr.next
        fast_ptr.next=slow_ptr.next
        slow_ptr.next=self.head




    def ptl(self):
        temp=self.head
        if self.head is not None:
            while True:
                print(temp.data,'-->',end=' ')
                temp=temp.next
                if temp==self.head:
                    break

            
                


head=CirLinkedList()
head1=CirLinkedList()
head2=CirLinkedList()
head.add_beg(3)
head.add_beg(4)
head.add_beg(2)
head.add_beg(5)
print('\nOriginal Circular Linked List')
head.ptl()
head.spllitlinked(head1,head2)
print('\nFirst:')
head1.ptl()
print('\nsecond')
head2.ptl()
