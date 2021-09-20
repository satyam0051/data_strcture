class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add_beg(self,nd):
        new_node=Node(nd)
        new_node.next=self.head
        self.head=new_node
    def prnt(self):
        temp=self.head
        while temp:
            print(temp.data,'-->',end=' ')
            temp=temp.next
    def revbyn(self,head,k):
        prev=None
        next=None
        curr=head
        c=1
        while c<=k:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            c=c+1

        if next is not None:
            head.next=self.revbyn(next,k)
        return prev

 






ll=linkedlist()
ll.add_beg(8)
ll.add_beg(7)
ll.add_beg(6)
ll.add_beg(5)
ll.add_beg(4)
ll.add_beg(3)
ll.add_beg(2)
ll.add_beg(1)
ll.prnt()
ll.revbyn(ll.head,3)
ll.prnt()



