# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:46:14 2018

@author: manoj
"""

from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser("Desciption: ")
ap.add_argument("-i","--image", required = True, help = "Provide path to the image")
b = vars(ap.parse_args())

image = cv2.imread(b["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(9,9),0) # blur with standard deviation sigma = 9
cv2.imshow("Blurred",blurred)
cv2.waitKey(0)

edge = cv2.Canny(blurred,30,150) # below 30 non edges and above 150 are sure edge
cv2.imshow("Canny_edged",edge)
cv2.waitKey(0)

(_,cnts,_) = cv2.findContours(edge.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # first argument we make a copy second argument is the outermost Contours
# third argument is the compress horizontal, vertical and diagonal segments into their end points only 
print("I count {} coins in the image".format(len(cnts)))
coins = image.copy()
#cv2.drawContours(coins,cnts,-1,(0,255,0),2) # first argument is the image second is the contours -1 means we want to draw all the Contours providing 1,2,3 .. will print the associated Contours
# fourth argument is the color we want to draw around the Contours. last argument is the thickness of our Contours

for i in range(0,len(cnts)):
 cv2.drawContours(coins,cnts,i,(0,255,0),2)
 cv2.imshow("Coins",coins)
 cv2.waitKey(0)

for (i, c) in enumerate(cnts):# we are iterating through our contours
 (x, y, w, h) = cv2.boundingRect(c) # x and y are starting point of rectangle in first contours

 print("Coin #{}".format(i + 1))
 coin = image[y:y + h, x:x + w] #cropping image as same height and width as the contours
 cv2.imshow("Coin", coin)

 mask = np.zeros(image.shape[:2], dtype = "uint8") #initialising mask of same height and width as image
 ((centerX, centerY), radius) = cv2.minEnclosingCircle(c) # extracting the centre of circle and radius of the circle
 cv2.circle(mask, (int(centerX), int(centerY)), int(radius),255, -1) #
 mask = mask[y:y + h, x:x + w]
 cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask)) # finally applying the AND operation on coins using mask
 cv2.waitKey(0)
 #Hello man what's u
 # I have made a second changes