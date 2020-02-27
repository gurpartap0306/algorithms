def count_sort(a,exp,b):
    i=0
    c=[]
    while i<10:
        c.append(0)
        i+=1
    i=0
    while i<len(a):
        c[(a[i]%(10**exp)//(10**(exp-1)))]+=1
        i+=1
    i=1
    while i<10:
        c[i]=c[i]+c[i-1]
        i+=1
    j=len(a)-1
    while j>=0:
        b[c[(a[j]%(10**exp)//(10**(exp-1)))]-1]=a[j]
        c[(a[j]%(10**exp)//(10**(exp-1)))]=c[(a[j]%(10**exp)//(10**(exp-1)))]-1
        j-=1
    print (b)
    return b

def main():
    a=[350,550,490,900,489]
    c=max(a)
    exp=0
    b=a.copy()
    while c>0:
        exp=exp+1
        c=c//10
        a=count_sort(a,exp,b)
    print(a)

if __name__=='__main__':
    main()
