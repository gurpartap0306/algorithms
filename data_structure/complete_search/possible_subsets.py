



def Search(n):
    lst=[]
    def recSearch(k):
        if k==n:
            print(lst)
        else:
            recSearch(k+1)
            lst.append(k)
            recSearch(k+1)
            lst.pop()

    recSearch(1)

if __name__=='__main__':
    Search(4)
