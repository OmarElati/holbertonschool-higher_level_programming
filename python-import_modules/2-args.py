#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    num_args = len(argv)
    if num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
    if num_args == 0:
        print(".")
    else:
        print("")
