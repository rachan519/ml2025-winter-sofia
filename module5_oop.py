class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        print(f"Enter {n} numbers:")
        for i in range(n):
            while True:
                try:
                    num = int(input(f"Number {i+1}: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

    def find_number(self, x):
        try:
            index = self.numbers.index(x) + 1  
            return index
        except ValueError:
            return -1


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
