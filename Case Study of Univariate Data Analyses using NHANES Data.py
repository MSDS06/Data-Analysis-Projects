#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[4]:


df = pd.read_csv("nhanes_2015_2016.csv")


# In[5]:


df.DMDEDUC2.value_counts()


# In[9]:


print(df.DMDEDUC2.value_counts().sum())
print(1621 + 1366 + 1186 + 655 + 643 + 3)
print(da.shape)


# In[10]:


pd.isnull(df.DMDEDUC2).sum()


# In[11]:


df["DMDEDUC2x"] = df.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 
                                       7: "Refused", 9: "Don't know"})
df.DMDEDUC2x.value_counts()


# In[12]:


df["RIAGENDRx"] = df.RIAGENDR.replace({1: "Male", 2: "Female"})


# In[13]:


x = df.DMDEDUC2x.value_counts()
x / x.sum()


# In[14]:


df.BMXWT.dropna().describe()


# In[18]:


x = df.BMXWT.dropna()
print(x.mean())


print(x.median())
print(np.percentile(x, 50))
print(np.percentile(x, 75))
print(x.quantile(0.75))


# In[19]:


np.mean((df.BPXSY1 >= 120) & (da.BPXSY2 <= 139))


# In[20]:


np.mean((df.BPXDI1 >= 80) & (da.BPXDI2 <= 89))


# In[27]:


a = (df.BPXSY1 >= 120) & (df.BPXSY2 <= 139)
b = (df.BPXDI1 >= 80) & (df.BPXDI2 <= 89)
print(np.mean(a | b))


# In[28]:


print(np.mean(da.BPXSY1 - df.BPXSY2))
print(np.mean(da.BPXDI1 - df.BPXDI2))


# In[29]:


sns.distplot(df.BMXWT.dropna())


# In[24]:


sns.distplot(df.BPXSY1.dropna())


# In[30]:


bp = sns.boxplot(data=df.loc[:, ["BPXSY1", "BPXSY2", "BPXDI1", "BPXDI2"]])
_ = bp.set_ylabel("Blood pressure in mm/Hg")


# In[31]:


df["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
plt.figure(figsize=(12, 5))
sns.boxplot(x="agegrp", y="BPXSY1", data=df)


# In[32]:


da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
plt.figure(figsize=(12, 5))
sns.boxplot(x="RIAGENDRx", y="BPXSY1", hue="agegrp", data=df)


# In[33]:


df.groupby("agegrp")["DMDEDUC2x"].value_counts()


# In[ ]:




