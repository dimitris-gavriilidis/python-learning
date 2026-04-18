'''
CS50P Week 1 - Math Interpreter
A program that uses an input formatted as x y z to perform calculation
if the user inputs 1 + 1, the program should output 2.0.
'''

math_expr = input("Expression: ")
x, y, z = math_expr.split()
x = int(x)
z = int(z)

if y == "+":
    print(f"{x+z:.1f}")
elif y == "-":
    print(f"{x-z:.1f}")
elif y == "*":
    print(f"{x*z:.1f}")
elif y == "/" and z != 0:
    print(f"{x/z:.1f}")