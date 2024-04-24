num1 =int(input("Enter first number: "))

num2 =int(input("Enter second number: "))

if(num1>num2):
    print("Greater number is " + str(num1))
else:
    print("Greater number is " + str(num2))


print(f"Greater number is {(max(num1,num2))}")

print("Greater number is:")
print(num1 if num1>num2 else num2)

x=[num1,num2]
x.sort()
print("Greater number is {}".format(x[-1]))