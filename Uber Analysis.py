#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


df = pd.read_csv("uber-raw-data-sep14.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info


# In[6]:


df.shape


# In[7]:


df.isnull()


# In[9]:


df["Date/Time"] = pd.to_datetime(df["Date/Time"])
df["Day"] = df["Date/Time"].apply(lambda x: x.day)
df["Hour"] = df["Date/Time"].apply(lambda x: x.hour)
df["Weekday"] = df["Date/Time"].apply(lambda x: x.weekday())


# In[10]:


df.head()


# In[13]:


df.describe()


# In[12]:


fig,ax = plt.subplots(figsize = (12,6))
plt.hist(df.Day, width= 0.6, bins= 30)
plt.title("Density of trips per Day", fontsize=16)
plt.xlabel("Day", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)


# In[14]:


fig,ax = plt.subplots(figsize = (12,6))
plt.hist(df.Weekday, width= 0.6, range= (0, 6.5), bins=7, color= "green")
plt.title("Density of trips per Weekday", fontsize=16)
plt.xlabel("Weekday", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)


# In[15]:


fig,ax = plt.subplots(figsize = (12,6))
plt.hist(df.Hour, width= 0.6, bins=24, color= "orange")
plt.title("Density of trips per Hour", fontsize=16)
plt.xlabel("Hour", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)


# In[17]:


fig,ax = plt.subplots(figsize = (12,6))
x= df.Lon
y= df.Lat
plt.scatter(x, y, color= "purple")
plt.title("Density of trips per Hour", fontsize=16)
plt.xlabel("Hour", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)


# In[ ]:




