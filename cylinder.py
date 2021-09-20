#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sep 2021
# This program calculates the volume of the cylinder
#    with the radius and height given by the user

import math


def main():
    # This function calculates the volume of the cylinder

    print("The Cylinder Volume Calculator")

    # input
    radius = int(input("Enter the radius (cm): "))
    height = int(input("Enter the height (cm): "))

    # process
    volume = (math.pi * radius ** 2) * height

    # output
    print("\nThe volume of the cylinder is {0} cm³.".format(volume))
    print("\nDone.")


if __name__ == "__main__":
    main()
