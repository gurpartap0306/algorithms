import rbTree

class node:
    def __init__(self,key):
        self.key=key
        self.p=None
        self.left=None
        self.right=None
        self.color='black'

class tree:
    def __init__(self):
        self.root=None
'''
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
    while z.p.color is 'red':
        if z.p==z.p.p.left:
            y=z.p.p.right
            if y.color is 'red':
                y.color='black'
                z.p.color='black'
                z.p.p.color='red'
                z=z.p.p
            else:
                if z is z.p.right:
                    z=z.p
                    left_rotate(t,z)
                z.p.color='black'
                z.p.p.color='red'
                right_rotate(t,z.p.p)
        else:
            y=z.p.p.left
            if y.color is 'red':
                y.color='black'
                z.p.color='black'
                z.p.p.color='red'
                z=z.p.p
            else:
                if z is z.p.left:
                    z=z.p
                    right_rotate(t,z)
                z.p.color='black'
                z.p.p.color='red'
                left_rotate(t,z.p.p)
    t.root.color='black'

def insert(t,z):
    y=node(None)
    x=t.root
    while x.key != None :
        y=x
        if z.key < x.key:
            x=x.left
        else: x=x.right
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
'''
def min(t):
    while t.left.key !=None:
        t=t.left
    return t

def transfer(t,u,v):
    if u.p.key is None:
        t.root=v
    elif u is u.p.left:
        u.p.left=v
    else: u.p.right=v
    v.p=u.p

def delete_fixup(t,x):
    while x.key is not None and x.color is 'black':
        if x is x.p.left:
            w = x.p.right
            if w.color is 'red':
                w.color='black'
                x.p.color='red'
                rbTree.left_rotate(t,x.p)
                w=x.p.right
            if w.left.color is 'black' and w.right.color is 'black':
                w.color = 'red'
                x=x.p
            else:
                if w.right.color is 'black':
                    w.left.color ='black'
                    w.color='red'
                    rbTree.right_rotate(t,w)
                    w=x.p.right
                w.color =x.p.color
                x.p.color ='black'
                w.right.color = 'black'
                rbTree.left_rotate(t,x.p)
                x=t.root
        else:
            w=x.p.left
            if w.color is 'red':
                w.color ='black'
                x.p.color='red'
                rbTree.right_rotate(t,x.p)
                w=x.p.left
            if w.left.color is 'black' and w.right.color is 'black':
                w.color ='red'
                x=x.p
            else:
                if w.left.color is 'black':
                    w.right.color='black'
                    w.color='red'
                    rbTree.left_rotate(t,w)
                    w=x.p.left
                w.color=x.p.color
                x.p.color ='black'
                w.left.color='black'
                rbTree.right_rotate(t,x.p)
                x=t.root
    x.color ='black'

def delete(t,z):
    y=z
    y_original_color=y.color
    if z.left.key is None:
        x=z.right
        transfer(t,z,z.right)
    elif z.right.key is None:
        x=z.left
        transfer(t,z,z.left)
    else:
        y=min(z.right)
        y_original_color=y.color
        x=y.right
        if y.p is z:
            x.p = y
        else:
            transfer(t,y,y.right_rotate)
            y.right=z.right
            y.right.p=y
        transfer(t,z,y)
        y.left=z.left
        y.left.p=y
        y.color=z.color
    if y_original_color is 'black':
        delete_fixup(t,x)


def main():
    t=tree()
    t.root=node(None)
    rbTree.rb_insert(t,node(2))
    rbTree.rb_insert(t,node(1))
    rbTree.rb_insert(t,node(4))
    rbTree.rb_insert(t,node(5))
    rbTree.rb_insert(t,node(9))
    rbTree.rb_insert(t,node(3))
    rbTree.rb_insert(t,node(6))
    rbTree.rb_insert(t,node(7))
    rbTree.rb_insert(t,node(15))
    delete(t,rbTree.search(t.root,7))
    rbTree.inorder(t.root)

if __name__=='__main__':
    main()
