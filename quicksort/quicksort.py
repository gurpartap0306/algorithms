def partition(a,p,r):
    x=a[r]
    i=p
    j=p
    while j<r:
        if a[j]<a[r] and a[i]>=a[j]:
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
            i+=1
        j+=1
    a[i],a[r]=a[r],a[i]
    #print (a,i)
    return i

def quicksort(a,p,r):
    if p<r-1:
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)

def main():
    #a=[2,8,7,3,5,6,]
    a=[3,6,8,8,6,2,0,4,12,65]
    quicksort(a,0,len(a)-1)
    print(a)

if __name__=='__main__':
    main()
