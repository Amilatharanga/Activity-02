<<<<<<< HEAD
#code 01
# Python program to display all the prime numbers within an interval

lower = 1000
upper = 1300

print("The Prime numbers from", lower, "to", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
=======
#code 02
# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum = sum + digit ** order
       temp //= 10

   if num == sum:
       print(num)
>>>>>>> m2
