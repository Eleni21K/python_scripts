'''
Ask the user for a number and determine whether the number is 
prime or not. (For those who have forgotten, a prime number is
 a number that has no divisors.)
'''

num = int(input("Please give a number: "))

i = num - 1
count = 0
while (i!=1):
	if num%i==0:
		print(num, "is not a prime")
		count = 1
		break
	i-=1

if count==0:
	print(num, "is a prime")
