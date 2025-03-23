import time
print("CALCULATOR")
Num1 = float(input("Enter the first number: ")) 
Num2 = float(input("Enter the second number: "))
oper = input("Enter operator: ")
if oper == "+":
    Answer = Num1 + Num2
    print(Num1,"+",Num2,"=",Answer)
elif oper == "-":
    Answer = Num1 - Num2
    print(Num1,"-",Num2,"=",Answer)
elif oper == "*":
    Answer = Num1 * Num2
    print(Num1,"*",Num2,"=",Answer)
elif oper == "/":
    Answer = Num1 / Num2
    print(Num1,"/",Num2,"=",Answer)

time.sleep(3)    

print("Now we hope you are satisfied with our calculator!")    