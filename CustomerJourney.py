#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.simplefilter(action="ignore")

import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.stats.api as sms
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind, mannwhitneyu


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

import matplotlib.pyplot as plt


# In[3]:


df_ = pd.read_excel("airlineSatisfactionAtilla06_Run.xlsx")


# In[4]:


df = df_.copy()


# In[6]:


df.shape


# In[7]:


df = df[df["Class"]=="Business"]


# In[8]:


df.shape


# In[9]:


df.head(30)


# In[10]:


df.index


# In[11]:


df['Inflight entertainment'].value_counts()


# In[12]:


df.columns


# In[13]:


target_columns = ['Inflight wifi service', 'Departure/Arrival time convenient',
       'Ease of Online booking', 'Gate location', 'Food and drink',
       'Online boarding', 'Seat comfort', 'Inflight entertainment',
       'On-board service', 'Leg room service', 'Baggage handling',
       'Checkin service', 'Inflight service', 'Cleanliness', 'satisfaction']


# In[14]:


for col in target_columns:
    df[col][df[col]==1] = 0
    df[col][df[col]==2] = 20
    df[col][df[col]==3] = 50
    df[col][df[col]==4] = 80
    df[col][df[col]==5] = 100
df.head()


# In[15]:


df['Inflight entertainment'].value_counts()


# In[16]:


df.head()


# In[17]:


df[target_columns].head()


# In[18]:


df[target_columns].corr()


# In[19]:


plt.figure(figsize=(20, 10))
sns.heatmap(df[target_columns].corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG');


# In[20]:


df_corr= df[target_columns].corr()
df_corr.head()


# In[21]:


df_final = df_corr[["satisfaction"]]
df_final.head(100)


# In[22]:


df_final.columns


# In[23]:


df_final.columns =  ["Importance"]
df_final.head()


# In[24]:


df[target_columns].mean()


# In[25]:


pd.DataFrame({"KolonAdi":df[target_columns].mean()})


# In[26]:


df[target_columns].std()


# In[27]:


pd.DataFrame({"Satisfaction": df[target_columns].mean(), "Service Quality": df[target_columns].std()})


# In[28]:


df_2 = pd.DataFrame({"Satisfaction": df[target_columns].mean(), "Service Quality": df[target_columns].std()})
df_2["Ratio"] = df_2["Service Quality"] / df_2["Satisfaction"]
df_2.head()


# In[29]:


df_final = df_final.join(df_2)
df_final.head()


# In[30]:


import matplotlib.pyplot as plt


# In[31]:


df_final.index


# In[32]:


target_columns_abv = ['IWS', 'DAC',
       'OBO', 'GL', 'FD',
       'OBR', 'SC', 'IE',
       'OBS', 'LRS', 'BH',
       'CS', 'IS', 'CLS', 'STS']


# In[33]:


df_final["Importance"]


# In[34]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10))

types = target_columns_abv
x_coords = df_final["Satisfaction"]
y_coords = df_final["Importance"]

plt.title("Satisfaction Map",size = 15)
plt.xlabel("Satisfaction",size = 15)
plt.ylabel("Importance",size = 15)


for i,type in enumerate(types):
    x = x_coords[i]
    y = y_coords[i]
    plt.scatter(x, y, marker='.', color='red')
    plt.text(x+0.01, y+0.01, type, fontsize=15)
    
    
plt.show()


# In[35]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10))


types = target_columns_abv
x_coords = df_final["Satisfaction"]
y_coords = df_final["Service Quality"]

plt.title("Service Quality Map")
plt.xlabel("Satisfaction")
plt.ylabel("Service Quality")


for i,type in enumerate(types):
    x = x_coords[i]
    y = y_coords[i]
    plt.scatter(x, y, marker='.', color='red')
    plt.text(x+0.02, y+0.02, type, fontsize=10)
plt.show()


# In[ ]:




