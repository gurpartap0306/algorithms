
def max_heapify(a,i):
    l=2*i+1
    r=2*i+2
    if l<len(a) and a[l] > a[i]:
        largest = l
    else: largest = i
    if r<len(a) and a[r]>a[largest]:
        largest=r
    if largest != i:
        a[i],a[largest] =a[largest],a[i]
        max_heapify(a,largest)


def build_max_heap(a):
    i=int((len(a)/2)-1)
    while i >=0:
        max_heapify(a,i)
        i-=1

def main():
    b=[]
    a=[16,4,10,14,7,9,3,2,8,1]
    build_max_heap(a)
    j=len(a)-1
    while j>=0:
        a[0],a[j]=a[j],a[0]
        b.append(a[j])
        a.pop(j)
        max_heapify(a,0)
        j-=1
    b.reverse()
    print (b)


if __name__=='__main__':
    main()
