# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:30:43 2021

@author: SESA619367
"""
import pandas as pd
import numpy as np

def naFiller(df,mode ='median',val =0):
    #mode =0
   
    nb_columns = len(df.columns)
    for i in range(nb_columns):
      if df.iloc[:,i].values.dtype != object :   
        if mode == 0 :           
            df.iloc[:,i].fillna(value =0,inplace =True)
        elif mode == 'mean':            
            df.iloc[:,i].fillna(value= df.iloc[:,i].mean(skipna = True), inplace=True)                        
        elif mode == 'median' :
            df.iloc[:,i].fillna(value=df.iloc[:,i].median(skipna = True), inplace=True)            
        elif mode == 'max' :
            df.iloc[:,i].fillna(value=df.iloc[:,i].max(skipna = True), inplace=True)          
        elif mode == 'min' :
            df.iloc[:,i].fillna(value=df.iloc[:,i].min(skipna = True), inplace=True)
        elif mode =='thresh':
            df.iloc[:,i].fillna(value=val, inplace=True)
    return(df)
    