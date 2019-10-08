#!/usr/bin/env python3

# Created by: Euel Yirga
# Created on: Oct 2019
# This does not crash when given invalid commands

def main():
    # this function uses a try statement

    # input
    integer_as_string = input("Enter an integer: ")
    print("")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        print("correct, this is an integer")
    except:
        print("This is not an integer")
    finally:
        print("Play another round")


if __name__ == "__main__":
    main()