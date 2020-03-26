# using dynamic programming

def lcs_length(x,y):
    m=len(x)+1
    n=len(y)+1
    b=[[None for x in range(1,n)] for y in range(1,m)]
    c=[[None for x in range(n)] for y in range(m)]
    for i in range(m):
        c[i][0]=0
    for i in range(1,n):
        c[0][i]=0
    for i in range(1,m):
        for j in range(1,n):
            if x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i-1][j-1]='LT'
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i-1][j-1]='T'
            else:
                c[i][j]=c[i][j-1]
                b[i-1][j-1]=' '
    return c,b

def print_lcs(b,x,i,j):
    if i==-1 or j==-1:
        return
    if b[i][j]=='LT':
        print_lcs(b,x,i-1,j-1)
        print (x[i])
    elif b[i][j]=='T':
        print_lcs(b,x,i-1,j)
    else: print_lcs(b,x,i,j-1)

def main():
    x='abcbdab'
    y='bdcaba'
    c,b=lcs_length(x,y)
    #for i in c: print(i)
    #for j in b:print(j)
    print_lcs(b,x,len(x)-1,len(y)-1)

if __name__=='__main__':
    main()
