def OddEve(n):
    if (n == 0):
        print("Zero")
    elif (round(n)%2 == 0):
        print("Even")
    else:
        print("Odd")
a = float(input())
OddEve(a)
