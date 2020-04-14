for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    earning=0
    lst.sort(reverse=True)
    for j in range(n):
        if lst[j]-j>0:
            earning+=lst[j]-j
    print(earning%1000000007)