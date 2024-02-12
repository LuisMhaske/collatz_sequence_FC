import sys

def collatz_sequence_length(x):
    length = 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x +1
        length += 1
    return length

def main():
    if len(sys.argv) != 2:
        print("Usage: python program_name.py x")
        print("x should be an integer from 1 to 100")
        return

    x = int(sys.argv[1])
    if not 1 <= x <= 100:
        print("Error: x should be an integer from 1 to 100")
        return

    sequence_length = collatz_sequence_length(x)
    print(f"Length of Collatz Sequence for {x}: {sequence_length}")

if __name__ == "__main__":
    main()