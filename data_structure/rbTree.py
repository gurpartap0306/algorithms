class node:
    def __init__(self,key):
        self.key=key
        self.color='black'
        self.p=None
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=node(None)

def left_rotate(t,x):
    y=x.right
    x.right=y.left
    if y.left.key is not None:
        y.left.p=x
    y.p=x.p
    if x.p.key is None:
        t.root=y
    elif x==x.p.left:
        x.p.left=y
    else: x.p.right=y
    y.left=x
    x.p=y

def right_rotate(t,x):
    y=x.left
    x.left=y.right
    if y.right.key is not None:
        y.right.p=x
    y.p=x.p
    if x.p.key is None:
        t.root=y
    elif x==x.p.left:
        x.p.left=y
    else: x.p.right=y
    y.right=x
    x.p=y

def rb_insert_fixup(t,z):
    while z.p.color=='red':
        if z.p==z.p.p.left:
            y=z.p.p.right
            if y.color == 'red':
                z.p.color='black'
                y.color='black'
                z.p.p.color='red'
                z=z.p.p
            else:
                if z==z.p.right:
                    z=z.p
                    left_rotate(t,z)
                z.p.color='black'
                z.p.p.color='red'
                right_rotate(t,z.p.p)

        else:
            y=z.p.p.left
            if y.color=='red':
                z.p.color='black'
                y.color='black'
                z.p.p.color='red'
                z=z.p.p
            else:
                if z==z.p.left:
                    z=z.p
                    right_rotate(t,z)
                z.p.color='black'
                z.p.p.color='red'
                left_rotate(t,z.p.p)
    t.root.color='black'


def rb_insert(t,z):
    y=node(None)
    x=t.root
    while x.key != None :
        y=x
        if z.key < x.key:
            x=x.left
        else: x=x.right
    #if x is not None: print(type(z.key))
    z.p=y
    if y.key==None:
        t.root=z
    elif z.key < y.key:
        y.left=z
    else: y.right=z
    z.left=node(None)
    z.right=node(None)
    z.color='red'
    rb_insert_fixup(t,z)

def inorder(t):
    if t is not None:
        inorder(t.left)
        if t.key is not None: print(t.key,t.color)
        inorder(t.right)

def search(t,z):
    if t.key ==None:
        return t
    if t.key==z: return t
    elif z<t.key:
        a= search(t.left,z)
    else: a= search(t.right,z)
    return a


def main():
    t=tree()
    rb_insert(t,node(2))
    rb_insert(t,node(1))
    rb_insert(t,node(4))
    rb_insert(t,node(5))
    rb_insert(t,node(9))
    rb_insert(t,node(3))
    rb_insert(t,node(6))
    rb_insert(t,node(7))
    rb_insert(t,node(15))
    '''#print(t.root.key)
    z=search(t.root,2)
    print (z.p.key)
    #inorder(t.root)
    print('********')
    right_rotate(t,z)
    #inorder(t.root)
    print(search(t.root,2).p.key)'''
    inorder(t.root)
    print(t.root.right.key)

if __name__=='__main__':
    main()
