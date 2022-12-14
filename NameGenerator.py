#!/usr/bin/env python3
__author__ = 'Aaron Otillar'

import random as rn


def generate_name():
    names = []
    with open("I:\\Python Projects\\ProgenGalaxy\\names.txt") as n:
	
        for line in n:
            data = n.readlines()

    for item in data:
        itemone = data.pop()
        itemtwo = itemone.replace('\n','')
        newdata = itemtwo.split()
        names.append(newdata.pop(0))
    length = len(names) - 1
    return names[rn.randrange(0,length)]
