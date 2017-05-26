#check whether an integer is a prime number or not
 
num = int(input("Enter number to check "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
          print(num,"Number is not prime")
          print(i,"times",num // i,"is",num)
          break
       else:
          print(num,"is a prime number")
else:
   print(num,"Number is not prime")
