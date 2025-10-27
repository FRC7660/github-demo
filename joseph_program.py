import sys

#!/usr/bin/env python3

def main():
    if len(sys.argv) >= 3:
        a, b ,c = sys.argv[1], sys.argv[2]
    else:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        c = input("Enter third number: ")
    try:
        a_num = float(a)
        b_num = float(b)
        c_num = float(c)
    except ValueError:
        print("Invalid number input.")
        sys.exit(1)

    result = a_num + b_num + c_num
    # print as int when it's a whole number
    if result.is_integer():
        result = int(result)
    print(result)

if __name__ == "__main__":
    main()
