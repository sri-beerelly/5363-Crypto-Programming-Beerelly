############################################
# Name: Srikanth Reddy Beerelly
# Class: CMPS 5363 Cryptography
# Date: 4 August 2015
# Program 3- Elliptical Curve
############################################



import argparse
import sys
import elliptical as el
# importing the fraction pacakge to use fractions in our program
from fractions import Fraction

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="x1 position on the curve")
    parser.add_argument("-y1",dest="y1", help="y1 position on the curve")
    parser.add_argument("-x2",dest="x2", help="x2 position on the curve ")
    parser.add_argument("-y2",dest="y2", help="y2 position on the curve")

    args = parser.parse_args()
    

    # Example:
    # python3 program_name.py -x1 2 -y1 3 -x2 -1 -y2 -1 -a 2 -b 1

    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)

    # Converting into fractios to take farctions and integers
    a = Fraction(args.a)
    b = Fraction(args.b)
    x1 = Fraction(args.x1)
    y1 = Fraction(args.y1)
    x2 = Fraction(args.x2)
    y2 = Fraction(args.y2)
    
    print(' ')
    print('Given Elliptical curve : y^2 = x^3+', a,'*x +', b)
    print(' ')

    # Calling a function to check whether both the points are on the curve or not
    points = el.checkPoints(x1,y1,x2,y2,a,b)
    

    


if __name__ == '__main__':
    main()
