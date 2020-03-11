#p=[1,5,8,9,10,17,17,20,24,30]
p=[1,5,8,10,17,20,24,30,35,22,75,38,65,33,78,97,102,111,114,115,75,119,120,123,124,125,126,131,163,176,188,191,200,205,210,244,256,275]

'''
#using recursion
def rod_cut(p,n):
    if n==0:
        return 0
    q=-9999
    i=1
    while i<=n:
        q=max(q,p[i-1]+rod_cut(p,n-i))
        i+=1
    return q
'''
#using dynamic programming
def rod_cut(p,n):
    r=[]
    for i in range(n):
        r.append(-999)
    return rod_cut_aux(p,n,r)

def rod_cut_aux(p,n,r):
    if r[n-1]>=0:
        return r[n-1]
    if n==0:
        q=0
    else:
        q=-999
        for i in range(1,n+1):
            q=max(q,p[i-1]+rod_cut_aux(p,n-i,r))
    r[n-1] = q
    return q

def main():
    n=30
    price=rod_cut(p,n)
    print (price)

if __name__=='__main__':
    main()
