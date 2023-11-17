#!/usr/bin/env python3
# Created by: Declan.Moher
# Created on: Nov. 10, 2023
# This program checks powers of two of user_number
def main():
    # tells you what the code runs
    print(
        "Hi USER!! Today we are going to be learning times tables of user_num, are you excited to start!!!"
    )

    # asking user for a positive number
    user_num_str = str(input(("Enter a positive number:")))
    try:
        # trying to put user_num into a integer
        user_num = int(user_num_str)

    except ValueError:
        # if user_num isn't a integer this will print
        print(f"{user_num_str} is not a valid number")
    else:
        # is user_num is greater or equal to zero count is going to start at -1
        if user_num >= 0:
            count = -1

            # creates a one time loop
            while True:
                count = count + 1
                product = user_num * count
                print(f"{count} * {user_num} = {product}")
                # if count reaches to 12 the loop would end
                if count == 12:
                    print("Congratulations on learning your multiples of 0 to 12")
                    break

        else:
            # otherwise if it is a negative number this will print
            print(f"{user_num} isn't a valid input please enter a positive number")


if __name__ == "__main__":
    main()
