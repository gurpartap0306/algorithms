class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

def insert(t,key):
    n=node(key)
    if t.root==None:
        t.root=n
    else:
        temp=t.root
        while temp != None:
            y=temp
            if key < temp.key: temp=temp.left
            else: temp = temp.right
        if key < y.key: y.left = n
        else: y.right = n

def inorder(temp):
    if temp != None:
        inorder(temp.left)
        print(temp.key)
        inorder(temp.right)



def main():
    t=tree()
    insert(t,6)
    insert(t,5)
    insert(t,2)
    insert(t,7)
    insert(t,8)
    insert(t,5)
    inorder(t.root)


if __name__=='__main__':
    main()
