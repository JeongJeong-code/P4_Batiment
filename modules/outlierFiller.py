# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:50:47 2021

@author: SESA619367
"""
import pandas as pd 
import numpy as np 


def outlierFiller(df,spot, mode, spot_value =0, thresh_value =0):
    nb_columns = len(df.columns)
    for i in range(nb_columns):
      if df.iloc[:,i].values.dtype != object :  
        mean = df.iloc[:,i].mean(skipna =True)    
        median = df.iloc[:,i].median(skipna =True)    
        first_quartile = np.nanpercentile(df.iloc[:,i],25)
        third_quartile =np.nanpercentile(df.iloc[:,i],75)
        std = df.iloc[:,i].std()
      
        if spot == 'third'  :  
            if mode =='0':
                df.iloc[df.iloc[:,i].values> 3*third_quartile,i] =0 
            
            elif mode =='median':
                df.iloc[df.iloc[:,i].values> 3*third_quartile,i] = median
        
            elif mode == 'third_quart' :
                df.iloc[df.iloc[:,i].values> 3*third_quartile,i] = third_quartile
                
            elif mode == 'drop' :
                df.iloc[df.iloc[:,i].values> 3*third_quartile,i].drop(axis =0, inplace =True)
            elif mode == 'thresh' :
                df.iloc[df.iloc[:,i].values> 3*third_quartile,i] = thresh_value
        elif spot =='std' :
            if mode =='0':
                df.iloc[df.iloc[:,i].values> third_quartile+3*std,i] =0 
            
            elif mode =='median':
                df.iloc[df.iloc[:,i].values> third_quartile+3*std,i] = median
        
            elif mode == 'third_quart' :
                df.iloc[df.iloc[:,i].values> third_quartile+3*std,i] = third_quartile
                
            elif mode == 'drop' :
                df.iloc[df.iloc[:,i].values> third_quartile+3*std,i].drop(axis =0, inplace =True)
            elif mode == 'thresh' :
                df.iloc[df.iloc[:,i].values> third_quartile+3*std,i] = thresh_value
        elif spot =='thresh' :
            if mode =='0':
                df.iloc[df.iloc[:,i].values> spot_value,i] =0 
            
            elif mode =='median':
                df.iloc[df.iloc[:,i].values> spot_value,i] = median
        
            elif mode == 'third_quart' :
                df.iloc[df.iloc[:,i].values> spot_value,i] = third_quartile
                
            elif mode == 'drop' :
                df.iloc[df.iloc[:,i].values> spot_value,i].drop(axis =0, inplace =True)
            elif mode == 'thresh' :
                df.iloc[df.iloc[:,i].values> spot_value,i] = thresh_value
        elif spot =='inter_quart':
            if mode =='0':
                df.iloc[df.iloc[:,i].values> median+1.5*round(third_quartile-first_quartile),i] =0 
            
            elif mode =='median':
                df.iloc[df.iloc[:,i].values> median+1.5*round(third_quartile-first_quartile),i] = median
        
            elif mode == 'third_quart' :
                df.iloc[df.iloc[:,i].values> median+1.5*round(third_quartile-first_quartile),i] = third_quartile
                
            elif mode == 'drop' :
                df.iloc[df.iloc[:,i].values> median+1.5*round(third_quartile-first_quartile),i].drop(axis =0, inplace =True)
            elif mode == 'thresh' :
                df.iloc[df.iloc[:,i].values> median+1.5*round(third_quartile-first_quartile),i] = thresh_value
    else :
       print('types non acceptés')

        
        
