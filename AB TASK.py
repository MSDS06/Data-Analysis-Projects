#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from statsmodels.stats import proportion as pr
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import statsmodels.stats.api as sms
warnings.filterwarnings("ignore")
pd.set_option("display.float.format" , lambda x: "%.6f" % x )
pd.set_option("display.width" , None)
pd.set_option("display.max_columns" , None)


# In[3]:


control_df = pd.read_excel("ab_testingHM11.xlsx" , sheet_name = "Control Group")


# In[4]:


test_df = pd.read_excel("ab_testingHM11.xlsx" , sheet_name = "Test Group")


# In[5]:


control_df.shape


# In[6]:


control_df.head()


# In[7]:


control_df.describe().T


# In[8]:


sns.distplot (control_df["Purchase"] , hist = False)
plt.show();


# In[9]:


test_df.head()


# In[10]:


control_df["Earning_Per_Click"] = control_df["Earning"] / control_df["Click"]


# In[11]:


control_df.head()


# In[12]:


test_df["Earning_Per_Click"] = test_df["Earning"] / test_df["Click"]
test_df.head()


# In[13]:


groups = [control_df, test_df]

for group in groups:
    group["Earning_Per_Click"] = group["Earning"] / group["Click"]

control_df.head ()
test_df.head ()


# In[14]:


control_df["Purchase"].describe ()


# In[15]:


test_df["Purchase"].describe ()


# In[16]:


desc_compare_df = pd.DataFrame ({"Control_Purchase": control_df["Purchase"].describe (),
                                 "Test_Purchase": test_df["Purchase"].describe ()})


# In[17]:


desc_compare_df


# In[18]:


sms.DescrStatsW (control_df["Purchase"]).tconfint_mean()


# In[19]:


earning_df = pd.DataFrame ({"Control_Earning": control_df["Earning"].describe (),
                            "Test_Earning": test_df["Earning"].describe ()})
earning_df


# In[20]:


control_df["Purchase"].head()


# In[21]:


sms.DescrStatsW (control_df["Earning"]).tconfint_mean ()


# In[22]:


sms.DescrStatsW (test_df["Earning"]).tconfint_mean ()


# In[23]:


from scipy.stats import shapiro


# In[24]:


p_value_threshold = 0.05


# In[25]:


shapiro (control_df['Impression'])


# In[26]:


ttest, p_value = shapiro (control_df['Impression'])


# In[27]:


ttest


# In[28]:


p_value


# In[29]:


if p_value >= p_value_threshold:
    print ("Normal")
else:
    print ("Abnormal")


# In[30]:


distribution_list = ("Normal")


# In[31]:


pd.DataFrame(index=['Impression'], data={"P_Value": p_value, "Distribution": distribution_list})


# In[32]:


def normality_func(dataframe):
    from scipy.stats import shapiro
    p_value_threshold = 0.05
    p_value_list = []
    distribution_list = []
    normal_list = []
    abnormal_list = []
    for col in dataframe.columns:
        ttest, p_value = shapiro (dataframe[col])
        p_value_list.append (p_value)
        if p_value >= p_value_threshold:
            distribution_list.append ("Normal")
            normal_list.append (col)
        else:
            distribution_list.append ("Abnormal")
            abnormal_list.append (col)

    new_df = pd.DataFrame (index=dataframe.columns, data={"P_Value": p_value_list, "Distribution": distribution_list})
    return new_df, normal_list, abnormal_list


# In[33]:


control_normality, control_normal_list, control_abnormal_list = normality_func (control_df)
test_normality, test_normal_list, test_abnormal_list = normality_func (test_df)


# In[34]:


control_normality


# In[35]:


control_normal_list


# In[36]:


control_abnormal_list


# In[37]:


from scipy.stats import levene

ttest_lev, p_value_lev = levene (control_df["Purchase"], test_df["Purchase"])


# In[38]:


def variance_homogeneity(dataframe_control, dataframe_test):
    from scipy.stats import levene
    p_value_threshold = 0.05
    p_value_list = []
    variance_list = []
    column_list = list (zip (sorted (dataframe_control.columns), sorted (dataframe_test.columns)))
    features = []
    homogeneus_list = []
    not_homogeneus_list = []
    for col in column_list:
        ttest_lev, p_value_lev = levene (dataframe_control[col[0]], dataframe_test[col[1]])
        if (col[0] == col[1]) and (p_value_lev >= p_value_threshold):
            p_value_list.append (p_value_lev)
            variance_list.append ("No Difference")
            homogeneus_list.append (col[0])
            features.append (col[0])
        elif (col[0] == col[1]) and (p_value_lev < p_value_threshold):
            p_value_list.append (p_value_lev)
            variance_list.append ("Different")
            not_homogeneus_list.append (col[0])
            features.append (col[0])

    new_df = pd.DataFrame (index=features, data={"P_Value": p_value_list, "Homogeneity_of_Variance": variance_list})

    return new_df, homogeneus_list, not_homogeneus_list


variance_df, homogeneus, not_homogeneus = variance_homogeneity (control_df, test_df)


# In[39]:


variance_df


# In[40]:


homogeneus


# In[41]:


not_homogeneus


# In[42]:


from scipy.stats import ttest_ind, mannwhitneyu


# In[43]:


ttest_ind (control_df["Click"], test_df["Click"], equal_var=False)
ttest_ind (control_df["Earning"], test_df["Earning"], equal_var=True)
ttest_ind (control_df["Impression"], test_df["Impression"], equal_var=True)
ttest_ind (control_df["Purchase"], test_df["Purchase"], equal_var=True)


# In[44]:


for a in control_df.columns :
    print(a)


# In[45]:



from scipy.stats import ttest_ind, mannwhitneyu
feat_dict = {}

for feat in control_normal_list:
    if feat in homogeneus:
        ttest_value, p_value = ttest_ind (control_df[feat], test_df[feat], equal_var=True)
        feat_dict[feat] = p_value
    elif feat not in homogeneus:
        ttest_value, p_value = ttest_ind (control_df[feat], test_df[feat], equal_var=False)
        feat_dict[feat] = p_value

for feat in control_abnormal_list:
    ttest_value, p_value = mannwhitneyu (control_df[feat], test_df[feat])
    feat_dict[feat] = p_value

ttest_df = pd.DataFrame (data=feat_dict.values (), index=feat_dict.keys (), columns=["Ttest_P_Value"])


# In[46]:


control_df["Impression"].mean()


# In[47]:


test_df["Impression"].mean()


# In[48]:


control_df["Click"].mean()


# In[49]:


test_df["Click"].mean()


# In[50]:


control_df["Purchase"].mean()


# In[51]:


test_df["Purchase"].mean()


# In[52]:


control_df["Earning"].mean()


# In[53]:


test_df["Earning"].mean()


# In[54]:


ttest_df


# In[55]:



for col in control_df.columns:
    ttest_df.loc[ttest_df.index == col, "Maximum Bidding Mean"] = control_df[col].mean ()


# In[56]:


ttest_df


# In[57]:



for col in test_df.columns:
    ttest_df.loc[ttest_df.index == col, "Average Bidding Mean"] = test_df[col].mean ()


# In[58]:


ttest_df


# In[59]:


threshold = 0.05        
ttest_df.loc[ttest_df["Ttest_P_Value"] < threshold, "H0_Hypothesis"] = "Rejected"
ttest_df.loc[ttest_df["Ttest_P_Value"] >= threshold, "H0_Hypothesis"] = "Not Rejected"


# In[60]:




ttest_df["Winner"] = ttest_df.apply (
    lambda x: "Maximum Bidding" if (x["Maximum Bidding Mean"] >= x["Average Bidding Mean"]) & (
                x["H0_Hypothesis"] == "Rejected") else
    "Average Bidding" if (x["Maximum Bidding Mean"] < x["Average Bidding Mean"]) & (
                x["H0_Hypothesis"] == "Rejected") else
    "No Difference", axis=1)

ttest_df


# In[ ]:




