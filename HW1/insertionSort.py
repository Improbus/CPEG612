#!/usr/bin/python

import sys


def iSort(a):

	inList = map(int, a.split())

	for i in range(len(inList)):
		print i
		compVal = inList[i]
		
		counter = i-1 
		print counter

		while (counter>=0 and inList[counter] > compVal):

			inList[counter+1] = inList[counter]

			counter = counter-1

		inList[counter+1] = compVal

	print inList

iSort(sys.argv[1])
