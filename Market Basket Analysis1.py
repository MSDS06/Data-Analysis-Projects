#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Business Problem
# Support(X, Y) = Freq(X,Y)/N
# Confidence(X, Y) = Freq(X,Y) / Freq(X)
# Lift = Support (X, Y) / ( Support(X) * Support(Y) )


# In[2]:


pip install mlxtend


# In[3]:


import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import warnings
warnings.filterwarnings ("ignore")


# In[4]:


df = pd.read_csv('Groceries_dataset.csv')
df.head()


# In[7]:


df["single_transaction"] = df["Member_number"].astype(str)+"_"+df["Date"].astype(str)

df.head()


# In[8]:


df2 = pd.crosstab(df['single_transaction'], df['itemDescription'])
df2.head()


# In[10]:


def encode(item_freq):
    res = 0
    if item_freq > 0:
        res = 1
    return res
    
basket_input = df2.applymap(encode)


# In[11]:


#Ready for Apriori 
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

frequent_itemsets = apriori(basket_input, min_support=0.001, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="lift")

rules.head()


# In[12]:


rules.sort_values(["support", "confidence","lift"],axis = 0, ascending = False).head(8)


# In[ ]:




