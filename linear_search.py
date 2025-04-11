def linear_searcher(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=list(map(int,input().split()))
target=int(input())
print( linear_searcher(arr,target))
