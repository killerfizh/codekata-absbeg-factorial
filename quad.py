def Quad(a,b,c):
  x1 = (-b + pow(pow(b,2)-(4*a*c), 0.5))/(2*a)
  x2 = (-b - pow(pow(b,2)-(4*a*c), 0.5))/(2*a)
  print("%.2f" % x1)
  print("%.2f" % x2)
  
p,q,r = map(float, input().split())
Quad(p,q,r)
