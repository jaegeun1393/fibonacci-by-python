n = int(input("Enter the number? "))
n1, n2 = 0, 1
count = 0

if n <= 0:
   print("Number is below 0.")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print("0")
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       total = n1 + n2
       n1 = n2
       n2 = total
       count += 1
