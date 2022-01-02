#!/usr/bin/env python
# coding: utf-8

# # United States - Crime Rates - 1960 - 2014

# ### Introduction:
# 
# This time you will create a data 
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/Laxminarayen/Inceptz-Batch13-Analytics_and_Python/master/08%20-%20Day%20-%208%20-%20Python%20Quiz%20Session/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv). 

# ### Step 3. Assign it to a variable called crime.

# In[19]:


df = pd.read_csv("https://raw.githubusercontent.com/Laxminarayen/Inceptz-Batch13-Analytics_and_Python/master/08%20-%20Day%20-%208%20-%20Python%20Quiz%20Session/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv")
df.head()


# ### Step 4. What is the type of the columns?

# In[20]:


df.info()  ##method 1


# In[4]:


df.dtypes ##method 2


# ##### Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
# 
# ### Step 5. Convert the type of the column Year to datetime64

# In[21]:


df['Year'] = pd.to_datetime(df['Year'],format ='%Y')


# In[22]:


df.head()


# In[7]:


df.dtypes


# ### Step 6. Set the Year column as the index of the dataframe

# In[23]:


df.set_index(['Year'],inplace=True)


# In[24]:


df.head()


# ### Step 7. Delete the Total column

# In[10]:


del df['Total']  ## Method 1


# In[13]:


df.drop("Total",axis =1,inplace=True) ## Method 2


# In[ ]:


df.loc[:,] ## Method 3


# ### Step 8. Group the year by decades and sum the values
# 
# #### Pay attention to the Population column number, summing this column is a mistake

# In[25]:


## Treat index as string and replace -1 to 0
## Method 1
crime_decades=df.groupby([int(str(i)[:-1])*10 for i in df.index.year]).sum()
crime_decades


# In[26]:


## Divide 1960 /10 = 196 then 196 *10
## Method 2
df.groupby((df.index.year//10)*10).sum()


# In[27]:


pop_grouped = df.groupby([int(str(i)[:-1])*10 for i in df.index.year])['Population'].max()
crime_decades['Population'] = pop_grouped
crime_decades


# ### Step 9. What is the mos dangerous decade to live in the US?

# In[28]:


crime_decades.idxmax()

