def Circum(r):
    if (r<0):
        print("Error")
    else:
        res = round(3.14159265359*r*2, 2)
        print(res)
a = float(input())
Circum(a)
