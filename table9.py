def Table9(n):
    tab = 9
    for i in range(1, n+1):
        tab = tab*i
        print(tab, end=" ")
num = int(input())
Table9(num)
