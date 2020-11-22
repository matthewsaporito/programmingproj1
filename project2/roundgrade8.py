#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:46:47 2020

@author: Sara Sterlie
"""


def roundGrade(data):
    gradesRounded = []
    for i in range(data[:,2:]):
        if i >= 11:
            i = 12
        if i < 11 or i >= 8.5:
            i = 10
        if i < 8.5 or i >= 5.5:
            i = 7
        if i < 5.5 or i >= 3:
            i = 4
        if i < 3 or i >= 1:
            i = 2
        if i < 1 or i >= -1.5:
            i = 0
        else:
            i = -3
        gradesRounded += [i]
    return gradesRounded

print(roundGrade(8))
