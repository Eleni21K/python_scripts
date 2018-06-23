'''
Ask the user for a string and print out whether this string is a 
palindrome or not. (A palindrome is a string that reads the same 
forwards and backwards.)
'''

word = str(input("Enter string: "))
palindrome = word[::-1]
print(palindrome)
if word == palindrome:
	print("This word is a palindrome")
else:
	print("This word is not a palindrome")

