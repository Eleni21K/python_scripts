'''
Write a program that asks the user how many Fibonacci numbers 
to generate and then generates them. Ask the user
to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the 
next number in the sequence is the sum of the previous two numbers
in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''


def fibona(n):

    i = 1
    if n == 0:
	    fibon = []
    elif n == 1:
        fibon = [1]
    elif n == 2:
        fibon = [1,1]
    elif n > 2:
        fibon = [1,1]
        while i<(n-1):
            fibon.append(fibon[i]+fibon[i-1])
            i += 1
    return fibon

x = int(input("Please give the number of Fibonnaci numbers you want to print: "))

print(fibona(x))
