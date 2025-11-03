import sys

def parse_number(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            raise ValueError(f"Invalid number: {s!r}")

def main():
    if len(sys.argv) >= 3:
        a_str, b_str = sys.argv[1], sys.argv[2]
    else:
        a_str = input("Enter first number: ").strip()
        b_str = input("Enter second number: ").strip()

    try:
        a = parse_number(a_str)
        b = parse_number(b_str)
    except ValueError as e:
        print(e)
        sys.exit(1)

    product = a * b
    print(product)

if __name__ == "__main__":
    main()