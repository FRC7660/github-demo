import sys

def main():
    # accept exactly two command-line arguments, or prompt interactively
    if len(sys.argv) == 3:
        a, b = sys.argv[1], sys.argv[2]
    elif len(sys.argv) > 3:
        print(f"Usage: {sys.argv[0]} <num1> <num2>")
        sys.exit(2)
    else:
        a = input("Enter first number: ")
        b = input("Enter second number: ")

    try:
        a_num = float(a)
        b_num = float(b)
    except ValueError:
        print("Invalid number input.")
        sys.exit(1)

    result = a_num + b_num
    # print as int when it's a whole number
    if result.is_integer():
        result = int(result)
    print(result)

if __name__ == "__main__":
    main()
