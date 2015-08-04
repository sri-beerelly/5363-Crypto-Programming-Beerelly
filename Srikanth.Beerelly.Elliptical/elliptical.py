############################################
# Name: Srikanth Reddy Beerelly
# Class: CMPS 5363 Cryptography
# Date: 4 August 2015
# Program 3- Elliptical Curve
############################################

import math
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

#@param int or fractions
# Check whether the given points are on the curve or not
# if points are present on the curve then finds slope and another point on the curve
#@prints slope,(x3,y3) and graph

def checkPoints(x1,y1,x2,y2,a,b):
    flag = 1
    while flag:
        # Checking for points on the curve or not
        if (y1**2-(x1**3+a*x1+b) == 0) and (y2**2-(x2**3+a*x2+b) == 0):
            
            print('Both points are on the curve!!')
            print(' ')

            #Callig slope function to get the slope
            M = slopeFinding(x1,y1,x2,y2,a)
            print('slope is:')
            print(Fraction(M).limit_denominator())
            print(' ')
            

            x3 = 0
            y3 = 0
            # Finding x3,y3 from formulae
            x3 = M**2 - x1 - x2
            y3 = M*(x3-x1) + y1
            

            print('x3 is:')
            print(Fraction(x3).limit_denominator())
            print(' ')
            
            print('y3 is:')
            print(Fraction(y3).limit_denominator())
            print(' ')

            # Finding the maximum value among all to make a proper width and height
            myList = [abs(x1),abs(x2),abs(x3),abs(y1),abs(y2),abs(y3)]
            maxNum = max(myList)
            
            # Width and height for plotting graph
            w = maxNum + 5
            h = maxNum + 5
            
            # Plotting the graph
            plotGraph(x1,x2,x3,y1,y2,y3,w,h,M,a,b)
            
    
            flag = 0
            
        else: # if points are not on the curve prompts a message to the person
            
            print('One or both points are not on the curve!! Please enter proper points.')
            flag = 0
            break
        

#@param int or fractions
#@returns slope m
def slopeFinding(x1,y1,x2,y2,a):
    
    m = 0
    flag = 1
    
    while flag:
        # if both the points are equal
        if x1 == x2 and y1 == y2:
            m = float(((3*(x1**2))+a))/float((2*y1))
            flag = 0
            
        # if bothe the are different                    
        elif x1 != x2 and y1 != y2:
            
            m = (float(y2-y1))/float((x2-x1))
            flag = 0
        # if x1 and x2 only equal 
        elif x1 == x2 and y1 != y2:
            print('Vertical line')
            print('Slope is undefined')
            flag = 0
            break
        # if y1 and y2 only equal
        else:
            print('horizontal line')
            m = 0
            flag = 0
        	
    return m

#@param int or fatctions
#@prints Graph
def plotGraph(x1,x2,x3,y1,y2,y3,w,h,m,a,b):

    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    an1 = plt.annotate("Srikanth Beerelly", xy=(-w+2 , h-2), xycoords="data",va="center", ha="center",bbox=dict(boxstyle="round", fc="w"))

    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x + b ), [0])


    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')

    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),)

    plt.plot(x2, y2,'ro')

    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),)

    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))

    # I hard coded the third point, YOU will use good ol mathematics to find
    # the third point
    plt.plot(x3, y3,'yo')

    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,x3+1),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),)

    # Show a grid background on our plot
    plt.grid()

    # Show the plot
    plt.show()

    
    


