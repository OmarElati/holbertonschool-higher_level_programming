#!/usr/bin/python3
def print_last_digit(number: int) -> int:
    last_digit = str(abs(number) % 10)
    print(last_digit)
    print(f"({len(last_digit)} chars long)")
