from Lab5 import *


def main():
    #finds the total of the first x integers
    test_numbers = 10
    print("The sum of the first " + str(test_numbers) + " is " + str(sum(test_numbers)))
    print()

    #finds the maximum number in a list
    test_list = [-5, 3000, 4750, 9000, 1250]
    print(test_list)
    print("The maximum number in this list is " + str(largest(test_list)))
    print()

    #counts the number of cannonballs in a stack of cannonballs
    test_height = 6
    print("Height is " + str(test_height))
    print("The number of cannonballs in this stack is " + str(countCannonballs(test_height)))
    print()

    #fibonacci number calculator
    print("You must enter an integer for the Fibonacci calculator to work")
    again = True
    while again == True:
        test_fibonacci = int(input("Enter an integer for the fibonacci calculator: "))
        if test_fibonacci == "":
            again = False
        print("The Fibonacci number for " + str(test_fibonacci) + " is " + str(fibonacci(test_fibonacci)))
        print()
        

main()
