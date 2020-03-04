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

def search(t,key):
    if t==None:
        return t
    elif t.key==key:
        return t
    else:
        if key<t.key:
            a=search(t.left,key)
        else: a=search(t.right,key)
    return a

def min(t):
    while t.left !=None:
        t=t.left
    return t

def delete(t,key):
    if t==None:
        return t
    elif key<t.key: t.left=delete(t.left,key)
    elif key>t.key: t.right=delete(t.right,key)
    else:
        if t.left is None:
            temp=t.right
            t=None
            return temp
        elif t.right is None:
            temp=t.left
            t=None
            return temp
        temp=min(t.right)
        t.key=temp.key
        t.right=delete(t.right,temp.key)
    return t



def main():
    t=tree()
    insert(t,6)
    insert(t,5)
    insert(t,2)
    insert(t,7)
    insert(t,8)
    insert(t,5)
    #inorder(t.root)
    t.root=delete(t.root,6)
    inorder(t.root)
    #a=search(t.root,5)
    #if a!=None: print(a.key)
    #else:print ('no element in tree')


if __name__=='__main__':
    main()
