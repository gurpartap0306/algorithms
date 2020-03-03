def linear_search(a,b):
    i=0
    c=[]
    while i<len(a):
        if a[i]==b:
            c.append(i)
        i+=1
    return c

def main():
    a=[4,3,6,8,1,9]
    c=linear_search(a,10)
    if len(c)==0:
        print('element not found')
    else:
        print ('element is present at pos:')
        for i in c:
            print(i)


if __name__=='__main__':
    main()
