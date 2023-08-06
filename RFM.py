#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd


# In[44]:


import numpy as np


# In[45]:


import seaborn as sns


# In[46]:


import datetime as dt


# In[47]:


import matplotlib.pyplot as plt


# In[48]:


df = pd.read_excel("RFM DENEME 123.xlsx",sheet_name="online retail ham")


# In[50]:


df.head()


# In[51]:


df.describe([0.01,0.25,0.50,0.75,0.99]).T


# In[15]:


df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])


# In[52]:


df = df[(df.Quantity>0) & (df.UnitPrice> 0)]
df = df.drop_duplicates()
df.isnull().sum()


# In[60]:


df['Total_Price'] = df['UnitPrice']*df['Quantity']


# In[61]:


df.head()


# In[62]:


#Timestamp('2011-12-09 12:50:00')      ("2011-31-12 11:59:00")
df['InvoiceDate'].max()


# In[64]:


today = dt.datetime(2011,12,31)


# In[65]:


RFM = df.groupby('CustomerID').agg({'InvoiceDate' : lambda day : (today - day.max()).days,
                                    'InvoiceNo': lambda num : len(num), 'Total_Price': lambda price : price.sum()})


# In[66]:


col_list = ['Recency','Frequency','Monetary']
RFM.columns = col_list


# In[68]:


col_list


# In[ ]:


# qcut=Quantile-based discretization function.


# In[69]:


RFM["R"] = pd.qcut(RFM["Recency"],5,labels=[5,4,3,2,1])


# In[72]:


RFM["F"] = pd.qcut(RFM["Frequency"],5,labels=[1,2,3,4,5])


# In[73]:


RFM["M"] = pd.qcut(RFM["Monetary"],5,labels=[1,2,3,4,5])


# In[75]:


RFM["RFM_Score"] = RFM["R"].astype(str) +RFM["F"].astype(str) + RFM["M"].astype(str)


# In[76]:


RFM


# In[77]:


seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At Risk',
    r'[1-2]5': 'Can\'t Loose',
    r'3[1-2]': 'About to Sleep',
    r'33': 'Need Attention',
    r'[3-4][4-5]': 'Loyal Customers',
    r'41': 'Promising',
    r'51': 'New Customers',
    r'[4-5][2-3]': 'Potential Loyalists',
    r'5[4-5]': 'Champions'
}


# In[78]:


seg_map


# In[80]:


RFM['Segment'] = RFM['R'].astype(str) + RFM['F'].astype(str)
RFM['Segment'] = RFM['Segment'].replace(seg_map, regex=True)
RFM.head()


# In[81]:


RFM.groupby('Segment').mean().sort_values('Monetary')


# In[ ]:




