#!/usr/bin/python

import sys

def iSort(a):

	inList = map(int, a.split())

	outList = [inList.pop()]

	if inList:
		for j in range(len(inList)):
			addVal = inList.pop()
			outList.append(addVal)

			for i in range(len(outList)):

				compVal = outList[i]

				counter = i-1

				while (counter>=0 and outList[counter] > compVal):
	
					outList[counter+1] = outList[counter]

					counter = counter-1

				outList[counter+1] = compVal
	print outList

iSort(sys.argv[1])
