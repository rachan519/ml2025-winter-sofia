# Function to get an input
def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit() or (user_input and user_input[0] == '-' and user_input[1:].isdigit()):
            return int(user_input)
        print("Invalid input! Please enter an integer.")

N = get_valid_input("Enter a positive integer N: ")

numbers = []
for i in range(N):
    num = get_valid_input(f"Enter number {i + 1}: ")
    numbers.append(num)

X = get_valid_input("Enter the number X to search: ")

if X in numbers:
    print(numbers.index(X))  
else:
    print(-1)
