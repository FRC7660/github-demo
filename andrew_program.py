import argparse
import cmath
from typing import Union

def sqrt_number(value: Union[str, int, float, complex]) -> Union[float, complex]:
    """Return the square root of value. Returns a real float when possible, otherwise a complex."""
    z = complex(value)
    r = cmath.sqrt(z)
    if abs(r.imag) < 1e-12:
        return float(r.real)
    return r

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute square root(s) of given number(s).")
    parser.add_argument("numbers", nargs="+", help="Numbers to compute square root for (e.g. 9 -4 2+3j)")
    args = parser.parse_args()

    for s in args.numbers:
        try:
            result = sqrt_number(s)
            print(f"sqrt({s}) = {result}")
        except Exception as e:
            print(f"error computing sqrt({s}): {e}")