#!/usr/bin/env python

import argparse
import random

parser = argparse.ArgumentParser(description='Arguments')
parser.add_argument('-g', '--gen', help='random generation',
                    action='store_true', default=True)
args = parser.parse_args()
args_var = vars(args)

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
    if args_var['gen']:
        res = randomGen(numPowerball, numRedball, lengthPowerball, lengthRedball)
        if res:
            print('{} {} {} {} {} - {}'.format(res[0], res[1], res[2], res[3], res[4], res[5]))
