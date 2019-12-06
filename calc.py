import sys
while True:
	print("\n\n*** Calculator ***")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Exit")
	print("Enter choice: ", end="")
	ch = int(input())
	if(ch == 1):
		print("Enter num 1: ", end = "")
		num1 = int(input())
		print("Enter num2: ", end = "")
		num2 = int(input())
		print("Additions of " + str(num1) + " & " + str(num2) + " is " + str(num1+num2))

	elif(ch == 2):
		print("Enter num 1: ", end = "")
		num1 = int(input())
		print("Enter num2: ", end = "")
		num2 = int(input())
		print("Subtraction of " + str(num1) + " & " + str(num2) + " is " + str(num1-num2))

	elif(ch == 3):
		print("Enter num 1: ", end = "")
		num1 = int(input())
		print("Enter num2: ", end = "")
		num2 = int(input())
		print("Multiplication of " + str(num1) + " & " + str(num2) + " is " + str(num1*num2))

	elif(ch == 4):
		print("Enter num 1: ", end = "")
		num1 = int(input())
		print("Enter num2: ", end = "")
		num2 = int(input())
		print("Division of " + str(num1) + " & " + str(num2) + " is " + str(num1/num2))

	elif(ch == 5):
		sys.exit(0)

	else:
		print("Wrong choice.\nTry again\n\n")