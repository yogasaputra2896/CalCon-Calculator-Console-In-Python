#Logo Ascii Art
def logo():
    print(""" 
----------------------------------------------
 dP""b8    db    88      dP""b8  dP"Yb  88b 88 
dP   `"   dPYb   88     dP   `" dP   Yb 88Yb88 
Yb       dP__Yb  88  .o Yb      Yb   dP 88 Y88 
 YboodP dP    Yb 88ood8  YboodP  YbodP  88  Y8 
----------------------------------------------
 CALCULATOR CONSOL BY DOYOK DEVELOPER v.1.0
----------------------------------------------
- Command :                  Example:
  >> Number                  >> 100
  >> Operator(+,-,*,/,%)     >> +
  >> Number                  >> 100
  >> Operator(=)             >> = 
  >> Result                  >> 200
  Tips:
  >> Calculator will continue to calculate 
     Until the operator (=) is given
-----------------------------------------------   
    """)

#Calculator
def calculator():
    #Try
    try:
        result = float(input(">> "))
        #Looping
        while True:
            operator = input(">> ").strip()
            if operator == '=':
                if result.is_integer():
                    result = int(result)
                print("----------------------------------------------- ")
                print(f"Result : {result}")
                print("----------------------------------------------- ")
                break
            elif operator in ('+', '-', '*', '/', '%'):
                num = float(input(">> "))
                if operator == '+':
                    result += num
                elif operator == '-':
                    result -= num
                elif operator == '*':
                    result *= num
                elif operator == '/':
                    if num == 0:
                        print("Invalid Input: Division by zero is not allowed")
                        continue
                    result /= num
                elif operator == '%':
                    result %= num
                
                if result.is_integer():
                    result = int(result)
                print(f"Current [{result}]")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

#Main
if __name__ == "__main__":
    logo()
    calculator()
