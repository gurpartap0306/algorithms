def count_sort(a,b,key):
    c=[]
    i=0
    while i <= key:               #make list c of length key+1
        c.append(0)
        i+=1
    i=0
    while i<len(a):                #c holds no of elements of particular values
        c[a[i]]=c[a[i]]+1
        i+=1
    i=1
    while i<= key:                    #c holds position of every value
        c[i]=c[i]+c[i-1]
        i+=1
    j=len(a)-1
    while j>=0:                     #put values in list b according to their position
        b[c[a[j]]-1]=a[j]
        c[a[j]]=c[a[j]]-1
        j-=1

def main():
    a=[2,5,3,0,2,3,0,3]
    b=a.copy()
    count_sort(a,b,5)
    print (b)

if __name__=='__main__':
    main()
