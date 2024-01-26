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
def sub(i,arr,a,n):
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
sub(0,arr,a,n)
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
##binary bits
'''def binary(i,n,res):
    if n==0:
        print(res)
        return
    p=bin(i)[2::]
    q=[]
    q.append(p.count("1"))
    res.append(*q.copy())
    binary(i+1,n-1,res)
res=[]
print(binary(1,5,res))'''
##COMBINATIONSL SUM
#te index can be considered as many tines as possibke and
#at end of each subset make sure to pop the lst and try to append new and
#after that index go to ind+1)
'''class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        def f1(i,arr,target,ds,res):
            if i==len(arr):
                if target==0:
                    res.append(ds.copy())
                return
            if arr[i]<=target:
                ds.append(arr[i])
                f1(i,arr,target-arr[i],ds,res)
                ds.pop()
            f1(i+1,arr,target,ds,res)
        ds=[]
        res=[]
        f1(0,arr,target,ds,res)
        return res'''
##combinationaal sum2
#only for unique occurences
#then we cn traverse from a new index to end every time
#as they gve in sortig dolist sort() first
'''class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        def f1(ind,arr,target,res,ds):
            if target==0:
                res.append(ds.copy())
                return
            for i in range(ind,len(arr)):
                if i>ind and arr[i]==arr[i-1]:
                    continue
                if arr[i]>target:
                    break
                ds.append(arr[i])
                f1(i+1,arr,target-arr[i],res,ds)
                ds.pop()
        ds=[]
        res=[]
        p=sorted(arr)
        f1(0,p,target,res,ds)
        return res'''
##


        

        



    
