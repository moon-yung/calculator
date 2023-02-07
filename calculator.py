def add(x,y):
    print(f"\n{num1} + {num2} = {num1+num2}")
    
def sub(x,y):
    print(f"\n{num1} - {num2} = {num1-num2}")

def mul(x,y):
    print(f"\n{num1} x {num2} = {num1*num2}")

def div(x,y):
    print(f"\n{num1} ÷ {num2} = {num1/num2}")

print("""\n  C   A   L   C   U   L   A   T   O   R

            '+' Addition
            '-' Subtraction
            '*' Multiplication
            '/' Division
            'E' Exit
            """)   

while True:
 
    num1 = float(input("\nENTER FIRST NUMBER: "))
 
    choice = input("Enter operation + - * / E:  ")
    
    if choice == "E" or choice == "e":
        print("\nExiting.......\n") 
        break

    if choice not in "+-*/":
        print("\nEnter only correct operation '+' '-' '*' '/'")
        continue

    num2 = float(input("ENTER SECOND NUMBER: ")) 
    
    if choice == "+":
        add(num1,num2)

    if choice == "-":
        sub(num1,num2)

    if choice == "*":
        mul(num1,num2)

    if choice == "/":
        div(num1,num2)


   
    




    
        

        
    




        




    

   
        