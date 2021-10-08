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