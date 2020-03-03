class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

def insert(l,a):
    n=node(a)
    t=l.head
    if(l.head==None):
        l.head=n
    else:
        while t.next != None:
            t=t.next
        t.next=n

def traverse(l):
    while l.head!=None:
        print(l.head.data)
        l.head=l.head.next

def delete(l,a):
    t=l.head
    if t==None:
        print('data underflow')
    else:
        i=0
        while i<a-1 and t!=None:
            t=t.next
            i+=1
        if t!=None:
            t1=t.next
            t.next=t1.next


def main():
    listt=linkedlist()
    for i in range(5):
        insert(listt,input())
    print('*********')
    delete(listt,3)
    traverse(listt)

if __name__=='__main__':
    main()
