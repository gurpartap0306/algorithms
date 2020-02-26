import heap_sort

#print maximum element from heap
def heap_maximum(a):
    return a[0]

#extract the maximum element from the heap
def heap_extract_max(a):
    if len(a)<1:
        return 'error: heap underflow'
    max =a[0]
    a[0]=a[len(a)-1]
    a.pop()
    heap_sort.max_heapify(a,0)
    return max

#increase the key value at position i in the heap 
def heap_increase_key(a,i,key):
    if key<a[i]:
        print ('error: new key is smaller than current key')
    a[i]=key
    while i>0 and a[heap_sort.parent(i)]<a[i]:
        a[i],a[heap_sort.parent(i)]=a[heap_sort.parent(i)],a[i]
        i=heap_sort.parent(i)

#insert new element in the heap
def max_heap_insert(a,key):
    a.append(-99999)
    heap_increase_key(a,len(a)-1,key)

def main():
    a=[16,14,10,8,7,9,3,2,4,1]
    heap_sort.build_max_heap(a)
    print(heap_maximum(a))  #print maximum element from heap
    print(heap_extract_max(a))  #extract the maximum element from the heap
    max_heap_insert(a,20)   #insert new element in the heap
    print(a)

if __name__=='__main__':
    main()
