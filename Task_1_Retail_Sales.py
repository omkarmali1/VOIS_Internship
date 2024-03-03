#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Loading Required Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


#Loading Data
df=pd.read_csv("Analysis of Super Store - DA.csv")


# In[5]:


#Viewing Dataset
df.head()


# In[6]:


df.tail()


# In[13]:


df.shape


# In[14]:


df.columns


# In[8]:


df['Ship Mode'].unique()


# In[9]:


df['State'].unique()


# In[10]:


df['Category'].unique()


# In[15]:


#Counting Null Values
df.isnull().sum()


# In[16]:


df.describe()


# In[17]:


df.info()


# In[18]:


df.duplicated().sum()


# In[19]:


df.drop(columns=['Postal Code'],inplace=True)


# In[21]:


df.head()


# In[24]:


df.groupby('Category').Quantity.count()


# In[25]:


df.groupby('Segment')['Category'].value_counts()


# In[38]:


#Getting Insignts from Graphical Representation of the Data


# In[22]:


plt.figure(figsize=(10,6))
sns.barplot(x=df['Category'],y=df['Sales'],data=df)


# In[26]:


plt.figure(figsize=(10,6))
sns.barplot(x=df['Category'],y=df['Profit'],data=df)


# In[27]:


plt.figure(figsize=(10,6))
sns.barplot(x=df['Category'],y=df['Discount'],data=df)


# In[30]:


plt.figure(figsize=(8,5))
sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
sales_by_region.plot(kind='bar', xlabel='Region', ylabel='Total Sales', title='Sales Performance by Region')
plt.show()


# In[31]:


plt.figure(figsize=(8,5))
segment_analysis = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)
segment_analysis.plot(kind='bar', xlabel='Segment', ylabel='Total Sales', title='Segment Analysis')
plt.show()


# In[33]:


plt.figure(figsize=(8,5))
sub_category_analysis = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
sub_category_analysis.plot(kind='bar', xlabel='Sub-Category', ylabel='Total Sales', title='Sub-Category Analysis')
plt.show()


# In[34]:


plt.figure(figsize=(8,5))
shipping_mode_analysis = df.groupby('Ship Mode')['Sales'].sum().sort_values(ascending=False)
shipping_mode_analysis.plot(kind='bar', xlabel='Shipping Mode', ylabel='Total Sales', title='Shipping Mode Analysis')
plt.show()


# In[36]:


plt.figure(figsize=(8,5))
city_insights = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)
city_insights.plot(kind='bar', xlabel='City', ylabel='Total Sales', title='Top 10 Cities by Sales')
plt.show()


# In[39]:


#Conclusions


# In[40]:


#1. From Furniture, Office Supplies and Technology Office supplies were sold the most but due to low costs it was not the best
#   category to increase the total sales.


# In[41]:


#2. Technology made the highest profits. In the technology category discounts offered were least.


# In[42]:


#3. Standard Class ship mode is preffered the most.


# In[43]:


#4. In the segment analysis Consumers stood out to be the segment with highest sales. 
#   Coorporate and Home Office also contributed well in increasing the sales. 


# In[44]:


#5. Phones and Chairs were sub-categories that contribute the most in sales.


# In[ ]:


#6. Top 10 Cities who contributed the most in increasing the sales were New York City, Los Angeles, Seattle, San Francisco,
#   Philadelphia, Houston, Chicago, San Diego, Jacksonville and Springfield

