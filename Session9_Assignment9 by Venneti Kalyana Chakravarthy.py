
# coding: utf-8

# In[23]:


#Read the dataset from the below link:

#https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv

import pandas as pd
import numpy as np

df_US_Baby_Namesdata=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')

print("Dataset information: \n",df_US_Baby_Namesdata.info())

df_US_Baby_Namesdata.head(2)


# In[25]:


#Question 1: Delete unnamed columns

df_US_Baby_Namesdata_DelCol=df_US_Baby_Namesdata.drop(['Unnamed: 0'],axis=1)
print("Data after deleted columns: \n")
df_US_Baby_Namesdata_DelCol.head()


# In[27]:


# Question 2: Show the distribution of male and female

print("Distribution of Male & Female: \n")
round(df_US_Baby_Namesdata['Gender'].value_counts(normalize=True)*100,2)


# In[29]:


# Question 3: Show the top 5 most preferred names

print("Top most preferred names: \n")

df_US_Baby_Namesdata[["Name","Count"]].groupby('Name').sum().sort_values("Count",ascending=0).head(5)


# In[31]:


# Question 4: What is the median name occurence in the dataset

df_US_Baby_Namesdata_median_Name=df_US_Baby_Namesdata[["Name","Count"]].groupby('Name').sum()

print("The median name occurence in the dataset: \n")
df_US_Baby_Namesdata_median_Name[df_US_Baby_Namesdata_median_Name['Count'] == df_US_Baby_Namesdata_median_Name['Count'].median()]


# In[33]:


#Question 5: Distribution of male and female born count by states


df_US_Baby_Namesdata_Gender_Distribution=df_US_Baby_Namesdata[['State','Gender','Count']].set_index(['State','Gender'])

print("Distribution of male and female born count by state: \n")

df_US_Baby_Namesdata_Gender_Distribution.groupby(['State','Gender']).sum()

