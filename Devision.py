try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
     
        result = num1 / num2
      
        print(f"The result of {num1} / {num2} is: {result}")

except ValueError:
    
    print("Error: Please enter valid numbers.")
