#!/usr/bin/env python

import random

def randomGen(nP, nR, lP, lR):
    if lP > nP or lR > nR:
        return False
    powerballs = random.sample(range(1, nP), lP)
    redballs = random.sample(range(1, nR), lR)
    return powerballs + redballs

if __name__ == '__main__':

    numPowerball = 69
    numRedball = 26
    lengthPowerball = 5
    lengthRedball = 1
    res = randomGen(numPowerball, numRedball, lengthPowerball, lengthRedball)
    if res:
        print('{} {} {} {} {} - {}'.format(res[0], res[1], res[2], res[3], res[4], res[5]))
