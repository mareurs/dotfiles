#!/usr/bin/env python
import math

dataL1 = dict()
dataL2 = dict()
f = open('example_file')


#Save data to dicts
def saveData():
    for line in f:
        if line[0] == '1':
            defDic = dataL1
        else:
            defDic = dataL2
        for word in line[2:].split():
            points = []
        for point in word.split(':'):
            points.append(point)
        defDic.setdefault(points[0], [])
        defDic[points[0]].append(float(points[1]))


def calculateVariance(points):
    theSum = 0
    theSTD = 0
    for point in points:
        theSum += point
    mean = theSum / len(points)
    for point in points:
        theSTD += (point - mean) * (point - mean)
    theSTD = math.sqrt(theSTD)
    return(mean, theSTD)

if __name__ == '__main__':
    saveData()
    ### Variance for Label 1

    print('Variance for Label 1')
    for key in dataL1.iterkeys():
        (mean, var) = calculateVariance(dataL1[key])
        print(key + ':' + str(var))

    print('Variance for Label -1')
    for key in dataL2.iterkeys():
        (mean, var) = calculateVariance(dataL2[key])
        print(key + ':' + str(var))
#pymode:folding=1
