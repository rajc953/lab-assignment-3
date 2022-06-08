print(' Simple Calculator ')
print('The program exits when an incorrect expression is entered or "Quit"')
while True:
    term_math = input('Enter a mathematical expression:')
    if term_math.lower() == 'quit':
        break
    print('Result :',eval(term_math))

# this can be done in another way
n1= int(input("enter the number"))
operator = input("enter the operator,+,-,*,/")
n2= int(input("enter the second number"))
if operator=="+":
    print(n1+n2)
elif operator=="-":
    print(n1-n2)
elif operator=="*":
    print(n1*n2)
elif operator=="/":
    print(n1/n2)
else:
    print("invalid operator")