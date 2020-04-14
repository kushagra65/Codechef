for t in range(int(input())):
    n=int(input())
    seq=int(n/2)
    if n==1:
        print(1)
        print(1,1)
    elif n==2:
        print(seq)
        print(2,1,2)
    elif n%2!=0:
        print(seq)
        for i in range(1, n + 1, 2):
            if i == 1:
                print(3, 1, i + 1, i + 2)
            elif i >= 4:
                print(2, i - 1, i)
    else:
        print(seq)
        for i in range(1, n + 1, 2):
            if i == 1:
                print(2, 1, i + 1)
            elif i >= 3:
                print(2, i, i+1)