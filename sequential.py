#!/usr/bin/env python3

IMAGE_SIZE   = 9
PALETTE_SIZE = 2

def generate():
    # Start with an empty image.
    image = [0] * IMAGE_SIZE

    # Keep track of the current iteration index.
    index = 0

    # The first iteration is all zeroes so we may as well output it now.
    print("{0:-<8} {1:}".format(index, image))

    while True:
        # Increment the index.
        index += 1

        # Increment the first pixel.
        image[0] += 1

        # Iterate and carry.
        for i in range(0, IMAGE_SIZE):
            if image[i] > PALETTE_SIZE - 1:
                image[i] = 0

                if i < IMAGE_SIZE:
                    image[i+1] += 1

        # Output the image for this index.
        print("{0:-<8} {1:}".format(index, image))

        # Stop if the whole image is equal to the last palette entry which
        # means we've reached the last iteration.
        if image[-1] == PALETTE_SIZE - 1 and image.count(image[0]) == len(image):
            break

if __name__ == "__main__":
    generate()
