#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:11:15 2020

@author: Matt
"""

import numpy as np
import math as m
import pandas as pd
from pandas import isnull
from pandas import NA
from data_load import filterData
from computeFinalGrade import computeFinalGrade

def displayGrades():
    
    data = filterData(log=False)
    finalgrade = computeFinalGrade()
    
    Framedata = pd.DataFrame(data)
    Framefinalgrade = pd.DataFrame(finalgrade)
    
    
    