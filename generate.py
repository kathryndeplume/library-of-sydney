#!/usr/bin/env python3

IMAGE_SIZE   = 3
PALETTE_SIZE = 3

import sys

def generate(index):
    return list(map(
            lambda i: int((index / (PALETTE_SIZE ** i)) % PALETTE_SIZE),
            range(0, IMAGE_SIZE)
        ))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <index>".format(sys.argv[0]))
        sys.exit(1)

    print(generate(int(sys.argv[1])))
