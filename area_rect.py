def Area_Rect(a, b):
    res = round(a*b, 1)
    if ((res-int(res))*10 == 0):
        print(int(res))
    else:
        print(res)
p = float(input())
q = float(input())
Area_Rect(p,q)
