n=int(input("how many times should the programme work?"))
for i in range(n):
      a=int(input("enter the first number"))
      b=int(input("enter the second number"))
      print("press 1 for addition")
      print("press 2 for subtraction")
      print("press 3 for multiplition")
      print("press 4 for division")
      y=int(input())
      if y==1:
            c=a+b
            print(c,"is the added value")
      if y==2:
            if a>b:
                  c=a-b
                  print(c,"is the subtracted value") 
            if b>a:
                  c=b-a
                  print(c,"is the subtracted value")
      if y==3:
            c=a*b
            print(c,"is the product")
      if y==4:
            if a>b:
                  c=a/b
                  print(c,"is the divided value") 
            if b>a:
                  c=b/a
                  print(c,"is the divided value")
      if y!=1 and y!=2 and y!=3 and y!=4:
            print("invalid choice")
          
      print("--------------------------------------------")     
f=open("data.txt","w")
f.write(str(c))
f.close()
