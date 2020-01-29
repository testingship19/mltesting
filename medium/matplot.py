#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"]=20,10


# In[ ]:





# In[3]:


#Loading the dataset from Github
url ="https://raw.githubusercontent.com/testingship19/mltesting/master/water_quality_of_tributary_streams_panchganga_and_bhima-2014.csv"
names = ['STATION CODE', 
         'LOCATIONS',
         'STATE',
         'TEMPMin',
         'TEMPMax',
         'TEMPMean',
         'DOMin',
         'DOMax',
         'DOMean',
         'pHMin',
         'pHMax',
         'pHMean',
         'CONDUCTIVITYMin',
         'CONDUCTIVITYMax',
         'CONDUCTIVITYMean',
         'BODMin',
         'BODMax',
         'BODMean',
         'NITRATEMin',
         'NITRATEMax',
         'NITRATEMean',
         'FECALCOLIFORMMin',
         'FECALCOLIFORMMax',
         'FECALCOLIFORMMean',
         'TOTALCOLIFORMMin',
         'TOTALCOLIFORMMax',
         'TOTALCOLIFORMMean',]
dataset = pd.read_csv(url, names=names) #areading CSV file using Pandas


# In[4]:


dataset #display dataset


# In[5]:


sns.lmplot(x='TEMPMean',
           y='pHMean',
           data=dataset,
           fit_reg=False,
           hue='LOCATIONS')  #scatter plotting with regression line as false


# In[10]:


stats_df = dataset.drop(['STATION CODE', #dropping unnecesary tables
                         'LOCATIONS', 
                         'STATE',
                         'TEMPMin',
                         'TEMPMax',
                         'DOMin',
                         'DOMax',
                         'pHMin',
                         'pHMax',
                         'BODMin',
                         'BODMax',
                         'NITRATEMin',
                         'NITRATEMax',
                         'FECALCOLIFORMMin',
                         'FECALCOLIFORMMax',
                         'TOTALCOLIFORMMin',
                         'TOTALCOLIFORMMax',], axis=1)
sns.boxplot(data=stats_df) #Boxplot


# In[11]:


f, axes = plt.subplots(1, 2) #making subplots (1 row, 3 columns)
sns.lmplot(  x='TEMPMean', y='pHMean', data=dataset, hue = 'LOCATIONS') #scatter with reg_line=true
sns.boxplot( y=dataset.TEMPMin, x=dataset.pHMean, data=dataset, orient='h', ax=axes[0]) #zeroth column
sns.distplot(dataset.pHMean,ax=axes[1]) #first column

sns.boxplot( y=dataset.TEMPMin,orient='h')


# In[12]:


g = sns.catplot(x='TEMPMean', y='pHMean', data=dataset,
                   hue='LOCATIONS',  # Color by stage
                   col='LOCATIONS',  # Separate by stage
                   kind='swarm') # sharing x axis


# In[13]:


sns.lmplot(x='TEMPMean', y='pHMean', data=dataset)


# In[106]:





# In[ ]:





# In[ ]:




