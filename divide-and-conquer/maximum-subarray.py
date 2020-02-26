
def findMaxCrossingSubarray(a,low,mid,high):
    left_sum = -9999999
    sum=0
    i=mid
    while i>=low:
        sum = sum+a[i]
        if sum> left_sum:
            left_sum=sum
            max_left=i
        i-=1
    right_sum=-999999
    sum =0
    j=mid+1
    while j<=high:
        sum=sum+a[j]
        if sum > right_sum:
            right_sum=sum
            max_right=j
        j+=1
    return(max_left,max_right,left_sum+right_sum)


def findMaxSubarry(a,low,high):
    if high==low:
        return (low,high,a[low])
    else:
        mid=(low+high)//2
        left_low,left_high,left_sum=findMaxSubarry(a,low,mid)
        right_low,right_high,right_sum=findMaxSubarry(a,mid+1,high)
        cross_low,cross_high,cross_sum=findMaxCrossingSubarray(a,low,mid,high)
        if left_sum >= right_sum and left_sum >=cross_sum:
            return(left_low,left_high,left_sum)
        elif right_sum >=left_sum and right_sum >= cross_sum:
            return(right_low,right_high,right_sum)
        else:
            return(cross_low,cross_high,cross_sum)


def main():
    a=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,6]
    (b,c,d)=findMaxSubarry(a,0,15)
    print(a[b:c+1],"   ",d)


if __name__=='__main__':
    main()
