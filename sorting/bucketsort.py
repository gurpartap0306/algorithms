
def bucket_sort(a):
    b=[[] for i in range(10)]
    i=0
    j=len(a)
    d=[]
    while i<j:
        c=int(a[i]*10)
        b[c].append(a[i])
        i+=1
    for i in b:
        i.sort()
        d.append(i)
        for j in i:
            print (j)

def main():
    a=[.34,.76,.88,.35,.46,.71,.13,.26]
    bucket_sort(a)

if __name__=='__main__':
    main()
