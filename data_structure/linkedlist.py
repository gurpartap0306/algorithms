class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

def insert(l,a):
    n=node(a)
    if(l.head==None):
        l.head=n
    else:
        n.next=l.head
        l.head=n

def traverse(l):
    while l.head!=None:
        print(l.head.data)
        l.head=l.head.next

def main():
    listt=linkedlist()
    for i in range(5):
        insert(listt,input())
    print('*********')
    traverse(listt)

if __name__=='__main__':
    main()
