#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# In[2]:


data = pd.read_csv('../all_movies_with_id.csv')

# In[3]:


data.head()

# In[4]:


data_comment = data[['Movie_Name', 'Comment']]

# In[5]:


data_comment.head()

# In[7]:


data_comment.describe()

# In[9]:


data_comment.info()

# In[10]:


data_comment.isnull().sum()

# In[13]:


data_comment = data_comment.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# In[14]:


data_comment.isnull().sum()

# In[15]:


print(data_comment.describe())

# In[ ]:
data_comment.to_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\MovieComment.csv', index=None, header=True)
