#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:11:15 2020

@author: Matt Saporito
"""
import os
import numpy as np
import math as m
import pandas as pd
from pandas import isnull
from pandas import NA
from methods.utils import *


#merge calculated finale grade with the rest of grade data to display

def displayGrades(finalgrade, data):
    finalgrade = pd.DataFrame(computeFinalGrades(data))

    finalgrade.columns=['Final Grade']

    db = pd.DataFrame(data)
    db.columns=['student ID', 'Name', *['Assignment ' + str(x) for x in range(1, len(data[0]) - 1)]]
    df = pd.concat([db, finalgrade], axis=1)  # concatenates calculates grades and input data
    pd.set_option("display.max_rows", None, "Display.max_columns",None, "display.width",2000)
    print(df.sort_values(['Name']))
    return df.sort_values(['Name'])

    # color = 'red' if val < 0 else 'black'
    # return 'color: %s' % color
    # s = df.style.applymap(color_negative_red)

    # return df

    # Sort by ascending student name
    # df.sort('student')
    # reverse ascending
    # df.sort('student', ascending=False)
