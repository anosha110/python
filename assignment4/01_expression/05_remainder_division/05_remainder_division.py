def main():
    divided:int=int(input("Please enter an integer to be divided: "))
    divisor:int=int(input("Please enter an integer to divided by: "))
    quotient:int = divided // divisor
    remainder:int = divided % divisor

    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))




if __name__ == '__main__':
    main()
