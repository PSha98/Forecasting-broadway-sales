#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:45:37 2022

@author: gautam
"""
import pandas as pd

df_a = pd.read_csv("show_data_new_1985_1990.csv")
df_b = pd.read_csv("show_data_new_1990_2000.csv")
df_c = pd.read_csv("show_data_new_2000_2010.csv")
df_d = pd.read_csv("show_data_new_2010_2022.csv")
result = pd.concat([df_a.iloc[:,1:],df_b.iloc[:,1:],df_c.iloc[:,1:],df_d.iloc[:,1:]], axis=0,  ignore_index=True)
result = result.astype({'season': 'int'})
result.to_csv('show_data_final.csv')
df = result[['name','theatre']]

ans = result[df.isin(df[df.duplicated()])].sort_values(by = 'name')
print(df.duplicated())