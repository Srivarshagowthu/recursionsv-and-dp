#reversing array
'''def reverse(i,j):
    if i>=j:
        print(a)
        return
    a[i],a[j]=a[j],a[i]
    reverse(i+1,j-1)
a=[1,2,3,4]
n=4
reverse(0,n-1)'''
#palindrom
'''def pali(i,n):
    if s[i]!=s[n-i-1]:
        return False
    return pali(i+1,n-1)
s="madam"
pali(0,5)'''
#subsequence
'''def sub(i,arr,a,n):
    if i==n:
        print(arr)
        return
    arr.append(a[i])
    sub(i+1,arr,a,n)
    arr.pop()
    sub(i+1,arr,a,n)
arr=[]
a=[1,2,3]
n=3
sub(0,arr,a,n)'''
##sum of subsequence
'''def sub(i,arr,a,n,s,su):
    if i==n:
        if s==su:
            print(arr)
        return
    arr.append(a[i])
    s+=a[i]
    sub(i+1,arr,a,n,s,su)
    s-=a[i]
    arr.pop()
    sub(i+1,arr,a,n,s,su)
arr=[]
a=[1,2,3]
n=3
s=0
su=3
sub(0,arr,a,n,0,su)'''
##subset sivisions
'''def sub(i,arr,a,n):
    if i==n:
        print(arr)
        return
    arr.append(a[i])
    sub(i+1,arr,a,n)
    arr.pop()
    sub(i+1,arr,a,n)
arr=[]
a=[1,2,4,8]
n=4
sub(0,arr,a,n)'''
##bubble sort
'''def bubbles(a,n):
    if n==1:
        return a
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    return bubbles(a,n-1)
   
        
a=[1,4,3,2,6]
n=5
print(bubbles(a,5))'''
##merge sort
'''def merge_sort(a):
    if len(a)<=1:
        return a
    p=len(a)//2
    left_h=a[:p]
    right_h=a[p:]
    left_h=merge_sort(left_h)
    right_h=merge_sort(right_h)
    return merge(left_h,right_h)
def merge(l,r):
    result=[]
    i,j=0,0
    while(i<len(l) and j<len(r)):
        if l[i]<r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    result.extend(l[i:])#for remaining elemnts
    result.extend(r[j:])
    return result
a=[10,20,2,3,4,6,8,56,89]
print(merge_sort(a))'''

        



    
