#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


# In[5]:


df = pd.read_csv('rides.csv')
df.head()


# In[6]:


df.isnull().sum()


# In[8]:


df = df.dropna()


# In[9]:


df


# In[10]:


demand = df["Riders Active Per Hour"]
supply = df["Drivers Active Per Hour"]

figure = px.scatter(df, x = "Drivers Active Per Hour",
                    y = "Riders Active Per Hour", trendline="ols", 
                    title="Demand and Supply Analysis")
figure.update_layout(
    xaxis_title="Number of Drivers Active per Hour (Supply)",
    yaxis_title="Number of Riders Active per Hour (Demand)",
)
figure.show()


# In[12]:


avg_demand = df['Riders Active Per Hour'].mean()
avg_supply = df['Drivers Active Per Hour'].mean()
pct_change_demand = (max(df['Riders Active Per Hour']) - min(df['Riders Active Per Hour'])) / avg_demand * 100
pct_change_supply = (max(df['Drivers Active Per Hour']) - min(df['Drivers Active Per Hour'])) / avg_supply * 100
elasticity = pct_change_demand / pct_change_supply

print("Flexibility in the number of active drivers per hour: {:.2f}".format(elasticity))


# In[13]:


df['Supply Ratio'] = df['Rides Completed'] / df['Drivers Active Per Hour']
df.head()


# In[14]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Drivers Active Per Hour'], 
                         y=df['Supply Ratio'], mode='markers'))
fig.update_layout(
    title='Supply Ratio vs. Driver Activity',
    xaxis_title='Driver Activity (Drivers Active Per Hour)',
    yaxis_title='Supply Ratio (Rides Completed per Driver Active per Hour)'
)
fig.show()


# In[ ]:




