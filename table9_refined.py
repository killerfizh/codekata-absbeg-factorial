def Table9(num):
  if num == 0:
    print()
  else:
    for i in range (1,num+1):
      if i == num:
        print(i*9)
      else:
        print(i*9,end = " ")
n = int(input())
Table9(n)
