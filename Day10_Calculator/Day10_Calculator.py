from art import logo


def calculate_function(first_number, second_number, operation):
    if operation == "+":
        final_answer = first_number + second_number
    elif operation == "-":
        final_answer = first_number - second_number
    elif operation == "*":
        final_answer = first_number * second_number
    elif operation == "/":
        final_answer = first_number / second_number
    else:
        final_answer = 0
    return final_answer

def calculator():
    print(logo)
    calc_continue = True
    first_number = float(input("What is the first number: "))
    while calc_continue:
        operation = input("+ \n- \n* \n/ \nPick an operation:  ")
        if operation != "+" and operation !=  "-" and operation !=  "*" and operation !=  "/":
            print("Invalid operation")
            operation = input("+ \n- \n* \n/ \nPick an operation:  ")
        second_number = float(input("What is the second number: "))
        final_answer = calculate_function(first_number, second_number, operation)

        print(f"{first_number} {operation} {second_number} = {final_answer}")

        calc_continue = input(f"Type 'y' to continue calculating with {final_answer}, or type 'n' to start a new calculation: ").lower()
        if calc_continue == "y":
            first_number = final_answer
        else:
            calc_continue = False
            print("\n"* 20)
            calculator()

calculator()