import math
f=open("data3.txt","w")
f.write("how many equations you have?")
n=int(input("how many equations you have?"))
for i in range(n+1):
   a=int(f.write(input("enter the value of a=")))
   f.write(str(a))
   b=int(f.write(input("enter the value of b=")))
   f.write(str(b))
   c=int(input("enter the value of c="))
   print("now our equation looks like -")
   print(a,"x2 +",b,"x +",c,"= 0")
   print("let's try to find out its roots")
   d=((b*b)-(4*a*c))
   if d>0:
      print("the roots are real and unequal")
      print("let's find out it's roots")
      f=math.sqrt(d)
      x1= -b+f//2*a
      x2= -b-f//2*a
      print(x1,x2, "are the roots of the quadratic equation")
   elif d == 0:
      print("the roots are real and equal")
      print("let's find out it's roots")
      f=math.sqrt(d)
      x1= -b+f//2*a
      x2= -b-f//2*a
      print(x1," ",x2, "are the roots of the quadratic equation")
   else:
      print("the roots are imaginary")
   print("----------------------------------------------")            
   f=open("data2.txt","w")
   f.write(str(x1))
   f.write(str(x2))
f.close()