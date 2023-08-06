#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns" , None)
import datetime as dt


# In[3]:


df_= pd.read_excel("online_retail_II.xlsx",
                       sheet_name= "Year 2009-2010")


# In[5]:


df = df_.copy()
df.head()


# In[9]:


df.isnull().sum()


# In[10]:


df = df[-df["Invoice"].str.contains("C" , na=False)]


# In[11]:


df["TotalPrice"] = df["Quantity"] *df["Price"]


# In[12]:


df.dropna(inplace=True)


# In[13]:


df.isnull().sum()


# In[15]:


df.shape


# In[25]:


df["InvoiceDate"].max()
today_datetime = dt.datetime(2010 , 12 , 11)
today_datetime


# In[26]:


df.groupby("Customer ID").agg({"InvoiceDate" : lambda date : (today_datetime - date.max()).days})


# In[28]:


df.groupby("Customer ID").agg({"Invoice" : lambda Invoice: Invoice.nunique() })


# In[29]:


df.groupby("Customer ID").agg({"Invoice" : lambda TotalPrice: TotalPrice.sum() })


# In[31]:


df.groupby("Customer ID").agg({"InvoiceDate" : lambda date : (today_datetime - date.max()).days,
                              "Invoice" : lambda Invoice: Invoice.nunique(),
                              "TotalPrice" : lambda TotalPrice: TotalPrice.sum()})


# In[32]:


rfm = df.groupby("Customer ID").agg({"InvoiceDate" : lambda date : (today_datetime - date.max()).days,
                              "Invoice" : lambda Invoice: Invoice.nunique(),
                              "TotalPrice" : lambda TotalPrice: TotalPrice.sum()})


# In[35]:


rfm.columns = ["Recency" , "Frequency" , "Monetary"]
rfm = rfm[(rfm["Monetary"]) > 0 & (rfm["Frequency"] > 0)]


# In[36]:


rfm


# In[51]:


rfm["RecencyScore"] = pd.qcut(rfm["Recency"] , 5 , labels=[5,4,3,2,1])


# In[52]:


rfm["FrequencyScore"] = pd.qcut(rfm["Frequency"].rank(method = "first") , 5 , labels=[1,2,3,4,5])


# In[53]:


rfm["MonetaryScore"] = pd.qcut(rfm["Monetary"] , 5 , labels=[1,2,3,4,5])


# In[54]:


rfm.head()


# In[56]:


rfm["segment"] = (rfm["RecencyScore"].astype(str) +
                    rfm["FrequencyScore"].astype(str))


# In[57]:


rfm


# In[59]:


rfm["segment"].value_counts()


# In[60]:


seg_map = {
    r"[1-2][1-2]" : "Hibernating",
    r"[1-2][3-4]" : "At_Risk",
    r"[1-2]5" : "Cant_Loose",
    r"3[1-2]" : "About to Sleep",
    r"33" : "Need_attention",
    r"[3-4][4-5]" : "Loyal_Costumer",
    r"41" : "promissing",
    r"51" : "New_Costumers",
    r"[4-5][2-3]" : "Potential_Loyalist",
    r"5[4-5]" : "Champion"
}


# In[62]:


rfm["Segment_Label"] = rfm["segment"].replace(seg_map , regex=True)


# In[63]:


rfm


# In[65]:


rfm.groupby("Segment_Label").agg({"Recency" : "median" , "Frequency" : "median" ,"Monetary" : "median"})


# In[ ]:




