# https://codeforces.com/contest/2170/problem/B

'''
* the maximum possible r-l+1 can be N-nums.count(0)
* for some i-th operation we add r-l+1 to the sum of elements 
* so the total sum is atleast r-l+1 + (N-1) (because we can do N-1 operations adding simply 1 to each element)
* so we need to maximize r-l+1 such that,  total >= r-l+1 + (N-1)
* total - (N-1) >= r-l+1  and r-l+1 <= N - nums.count(0)
* thus maximum r-l+1 such that r-l+1 <= total - (N-1) and r-l+1 <= N - nums.count(0)
'''

def function(N,arr):
    ans,total = N-arr.count(0), sum(arr)
    for length in range(ans,0,-1):
        if total - (N-1) >= length:
            return length

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(function(N,arr))
    
