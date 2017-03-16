#Ismael Garrido pi_approximation.py

def main():
    print("This program approximates the value of pi")
    print("by summing a series of n terms to an extent determined by the user")
    terms = int(input("Please enter the amount of iterations you want the program to make: "))
    result = 0
    sign = 1
    for n in range(terms):
        result += sign/(2*n+1)
        sign = -sign
    print("The approximated value of pi is", 4*result)

main()

"""
This program approximates the value of pi
by summing a series of n terms to an extent determined by the user
Please enter the amount of iterations you want the program to make: 1
The approximated value of pi is 4.0
>>> main()
This program approximates the value of pi
by summing a series of n terms to an extent determined by the user
Please enter the amount of iterations you want the program to make: 2
The approximated value of pi is 2.666666666666667
>>> main()
This program approximates the value of pi
by summing a series of n terms to an extent determined by the user
Please enter the amount of iterations you want the program to make: 3
The approximated value of pi is 3.466666666666667
>>> main()
This program approximates the value of pi
by summing a series of n terms to an extent determined by the user
Please enter the amount of iterations you want the program to make: 4
The approximated value of pi is 2.8952380952380956
"""
