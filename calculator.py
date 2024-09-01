
# calculator.py

def add(num_a , num_b):
    res = num_a + num_b
    return res

def sub(num_a , num_b):
    res = num_a - num_b
    return res

def mul(num_a , num_b):
    res = num_a * num_b
    return res

def div(num_a , num_b):
    if num_b != 0:
        res = num_a / num_b
        return res
    else:
        return "Cannot divide by 0"

def main():
    print("Simple Calculator")
    print("Please select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1 , 2 ,3 ,4)  ")

    num_one = float(input("Enter first Number  "))
    num_two = float(input("Enter second Number  "))    

    if choice == '1' :
        add_res = add(num_one,num_two)
        print(f"Addition of {num_one} and {num_two} is {add_res}")
    
    elif choice == '2' :
        sub_res = sub(num_one,num_two)
        print(f"Subtraction of {num_one} and {num_two} is {sub_res}")
    
    elif choice == '3' :
        mul_res = mul(num_one,num_two)
        print(f"Multiplication of {num_one} and {num_two} is {mul_res}")
    
    elif choice == '4' :
        div_res = div(num_one,num_two)
        print(f"Divison of {num_one} and {num_two} is {div_res}")
    
    else:
        print("Invalid Input")

if __name__=='__main__':
    main()