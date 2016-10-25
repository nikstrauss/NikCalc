print ('Welcome to NikCalc!')
x = input('Enter your first number:' )
op = input('Enter the operand: ')
y = input('Enter the second number: ')
x = int(x)
y = int(y)
if op == ('+'):
	print (x + y)
elif op == ('-'):
	print (x - y)
elif op == ('*'):
	print (x * y)
elif op == ('/'):
	print (x / y)
else:
	print ("wrong op.")
input('Press any button to exit.')

