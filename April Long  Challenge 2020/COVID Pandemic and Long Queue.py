# cook your dish here

for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    flag=0
    no=0
    count=0
    for j in range(n):
        if lst[j]==1 and flag==0:
            count=1
            flag=1
        elif lst[j]==0 and flag==1:
            #print("runs")
            count+=1
        elif lst[j]==1 and flag==1:
            if count<6:
                #print("cout",count)
                print("NO")
                no=1
                break
            elif count>=6:
                #print(count,"co")
                count=1
    if no==0:
        print("YES")