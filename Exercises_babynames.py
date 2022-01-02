#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# US - Baby Names


# ### Introduction:
# 
# We are going to use a subset of [US Baby Names](https://www.kaggle.com/kaggle/us-baby-names) from Kaggle.  
# In the file it will be names from 2004 until 2014
# 
# 
# ### Step 1. Import the necessary libraries

# In[2]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/Laxminarayen/Inceptz-Batch13-Analytics_and_Python/master/08%20-%20Day%20-%208%20-%20Python%20Quiz%20Session/06_Stats/US_Baby_Names/US_Baby_Names_right.csv). 

# ### Step 3. Assign it to a variable called baby_names.

# In[3]:


baby_names = pd.read_csv('https://raw.githubusercontent.com/Laxminarayen/Inceptz-Batch13-Analytics_and_Python/master/08%20-%20Day%20-%208%20-%20Python%20Quiz%20Session/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')


# ### Step 4. See the first 10 entries

# In[4]:


baby_names.head(10)


# ### Step 5. Delete the column 'Unnamed: 0' and 'Id'

# In[5]:


baby_names.drop(['Unnamed: 0','Id'],axis=1,inplace=True)


# ### Step 6. Is there more male or female names in the dataset?

# In[6]:


baby_names.groupby('Gender').count()


# ### Step 7. Group the dataset by name and assign to names

# In[7]:


baby_names.groupby('Name').count().sort_values(by='Count',ascending=False)
   


# ### Step 8. How many different names exist in the dataset?

# In[8]:


baby_names['Name'].drop_duplicates().count()


# ### Step 9. What is the name with most occurrences?

# In[9]:


baby_names['Name'].mode()


# ### Step 10. How many different names have the least occurrences?

# In[10]:


baby_names.sort_values(by='Name',ascending=True).head()


# ### Step 11. What is the median name occurrence?

# In[20]:


baby_names.sort_values(by='Count',ascending=True).median()


# ### Step 12. What is the standard deviation of names?

# In[14]:


baby_names['Count'].std()


# ### Step 13. Get a summary with the mean, min, max, std and quartiles.

# In[51]:


baby_names.describe().T

