#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    total = sum(map(int, args))

    print("Somme des arguments : {}".format(total))

