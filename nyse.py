#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:14:24 2019

@author: sufyjakate
"""
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
sns.set(color_codes=True)

prices_df = pd.read_csv("prices.csv")
#print(prices_df)
wltw_df = prices_df[prices_df['symbol'] == 'WLTW']
print(wltw_df.volume)

sns.set(style="ticks")

sns.distplot(wltw_df.volume)
