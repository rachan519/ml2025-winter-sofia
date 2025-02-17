from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()
    
    while True:
        try:
            n = int(input("Enter the number of values (N): "))
            if n <= 0:
                raise ValueError("N must be a positive integer.")
            break
        except ValueError as e:
            print(e)
    
    processor.read_numbers(n)
    
    while True:
        try:
            x = int(input("Enter the number to search for (X): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    result = processor.find_number(x)
    print(result)


if __name__ == "__main__":
    main()
