#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis (EDA) on Hepatitis Data

# ## Library used
# 

# In[1]:


import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


# ## importing the data 

# In[2]:


hpts_data=pd.read_csv("C:\\Users\\Administrator\\Desktop\\hepatitiscsv.csv")


# ## Understanding the data 

# In[5]:


hpts_data


# In[6]:


hpts_data.head()


# In[7]:


hpts_data.describe()


# In[8]:


hpts_data.info()


# # Replacing the Values-- Data Cleaning - Modifiying

# In[ ]:





# In[11]:


hpts_data = hpts_data.replace({True: 1, False: 0})


# In[15]:


hpts_data.info()


# In[16]:


hpts_data['class'] = hpts_data['class'].replace(['live','die'],['1','0'])


# In[17]:


hpts_data


# In[18]:


hpts_data['sex'] = hpts_data['sex'].replace(['male','female'],['1','0'])


# In[19]:


hpts_data.info()


# In[20]:


hpts_data['class'] = hpts_data['class'].astype(float)
hpts_data['sex'] = hpts_data['sex'].astype(float)


# In[21]:


hpts_data.info()


# # Checking the Null Values & replacing with distribution  

# In[22]:


hpts_data.isna().sum()


# In[23]:


hpts_data


# # There are Two Type of Variable 
# 
# ## 1.Catagorical 
# ## 2.continuous
# 
# ## We need to impute the missing values ,depends on their distributions- Skewness

# In[ ]:





# # 1.Catagorical 

# In[ ]:





# In[ ]:





# In[25]:


hpts_data['steroid'].mode()


# In[26]:


hpts_data['steroid'].replace(to_replace=np.nan,value=1,inplace=True)


# In[27]:


hpts_data['fatigue'].mode()


# In[28]:


hpts_data['fatigue'].replace(to_replace=np.nan,value=0,inplace=True)


# In[29]:


hpts_data['malaise'].mode()
hpts_data['malaise'].replace(to_replace=np.nan,value=1,inplace=True)


# In[30]:


hpts_data['anorexia'].mode()
hpts_data['anorexia'].replace(to_replace=np.nan,value=1,inplace=True)


# In[31]:


hpts_data['liver_big'].mode()
hpts_data['liver_big'].replace(to_replace=np.nan,value=1,inplace=True)


# In[32]:


hpts_data['liver_firm'].mode()
hpts_data['liver_firm'].replace(to_replace=np.nan,value=1,inplace=True)


# In[33]:


hpts_data['spleen_palpable'].mode()
hpts_data['spleen_palpable'].replace(to_replace=np.nan,value=1,inplace=True)


# In[34]:


hpts_data['spiders'].mode()
hpts_data['spiders'].replace(to_replace=np.nan,value=1,inplace=True)


# In[35]:


hpts_data['ascites'].mode()
hpts_data['ascites'].replace(to_replace=np.nan,value=1,inplace=True)


# In[36]:


hpts_data['varices'].mode()
hpts_data['varices'].replace(to_replace=np.nan,value=1,inplace=True)


# In[37]:


hpts_data.info()


# # 2.Continuous

# In[38]:


hpts_data['bilirubin'].skew(axis=0,skipna = True) #Checking the Skewness


# In[39]:


hpts_data['bilirubin'].median()


# In[40]:


hpts_data['bilirubin'].replace(to_replace=np.nan,value=1,inplace=True) 


# In[41]:


hpts_data['alk_phosphate'].skew(axis=0,skipna = True) #Checking the Skewness


# In[42]:


hpts_data['alk_phosphate'].median()


# In[43]:


hpts_data['alk_phosphate'].replace(to_replace=np.nan,value=1,inplace=True)


# In[44]:


hpts_data['sgot'].skew(axis=0,skipna = True) #Checking the Skewness


# In[45]:


hpts_data['sgot'].median()


# In[46]:


hpts_data['sgot'].replace(to_replace=np.nan,value=58,inplace=True)


# In[47]:


hpts_data['albumin'].skew(axis=0,skipna = True) #Checking the Skewness


# In[48]:


hpts_data['albumin'].mean()


# In[49]:


hpts_data['albumin'].replace(to_replace=np.nan,value=4,inplace=True)


# In[50]:


hpts_data['protime'].skew(axis=0,skipna = True) #Checking the Skewness


# In[51]:


hpts_data['protime'].mean()


# In[52]:


hpts_data['protime'].replace(to_replace=np.nan,value=61,inplace=True)


# In[53]:


hpts_data.info()


# In[54]:


hpts_data.isnull().sum() # Checking the Missing Values 


# In[55]:


hpts_data.head()


# # Data Visualization

# In[ ]:





# In[56]:


plt.figure(figsize=(15,12))
sns.heatmap(hpts_data.corr(), cmap='coolwarm',linewidths=.1,annot = True)
plt.show()


# In[59]:


alk_phosphate = hpts_data["alk_phosphate"]
Class = hpts_data["class"]
correlation = alk_phosphate.corr(Class)
#calculate correlation between `column_1` and `column_2`
print(correlation)


# In[64]:


#Plot Pie Chart of Sex Column

male =len(hpts_data[hpts_data['sex'] == 0])
female = len(hpts_data[hpts_data['sex']==1])

plt.figure(figsize=(8,6))

# Data to plot
labels = 'Male','Female'
sizes = [male,female]
colors = ['red', 'yellowgreen']
explode = (0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=90)
 
plt.axis('equal')
plt.show()


# In[65]:


plt.figure(figsize=(10,8))
sns.scatterplot(x='age',y='bilirubin',data = hpts_data,hue = 'class')
plt.title('Bilirubin test values according to AGE')
plt.show()


# In[66]:


plt.figure(figsize=(10,8))
sns.scatterplot(x='age',y='alk_phosphate',data = hpts_data,hue = 'class')
plt.title('alk_phosphate test values according to AGE')
plt.show()


# In[67]:


plt.figure(figsize=(10,8))
sns.scatterplot(x='age',y='sgot',data = hpts_data,hue = 'class')
plt.title('sgot test values according to AGE')
plt.show()


# In[68]:


plt.figure(figsize=(10,8))
sns.scatterplot(x='age',y='protime',data = hpts_data,hue = 'class')
plt.title('protime values according to AGE')
plt.show()


# # Corr Plot for Continuous Variable

# In[ ]:





# In[71]:


DataFrame = pd.DataFrame(hpts_data,columns=['age','bilirubin','alk_phosphate','sgot','albumin','protime'])

corrMatrix = DataFrame.corr()
sns.heatmap(corrMatrix, annot=True)
plt.show()


# In[73]:


#Pie Plot for % of Die and Live

die =len(hpts_data[hpts_data['class'] == 0])
live = len(hpts_data[hpts_data['class']== 1])

plt.figure(figsize=(16,10))

# Data to plot
labels = 'DIE','LIVE'
sizes = [die,live]
colors = ['orange', 'lightgreen']
explode = (0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('% of Die & Live')
 
plt.axis('equal')
plt.show()


# In[75]:


plt.figure(figsize=(15,6))
sns.countplot(x='age',data = hpts_data, hue = 'steroid')
plt.title('count plot to visualize consumption of steriod in relation with Age')
plt.show()


# In[76]:


plt.figure(figsize=(15,6))
sns.countplot(x='age',data = hpts_data, hue = 'antivirals')
plt.title('count plot to visualize antivirals in relation with Age')
plt.show()


# In[77]:


plt.figure(figsize=(15,6))
sns.countplot(x='age',data = hpts_data, hue = 'fatigue')
plt.title('count plot to visualize fatigue in relation with Age')
plt.show()


# In[78]:


plt.figure(figsize=(15,6))
sns.countplot(x='age',data = hpts_data, hue = 'malaise')
plt.title('count plot to visualize malaise in relation with Age')
plt.show()


# In[79]:



plt.figure(figsize=(15,6))
sns.countplot(x='age',data = hpts_data, hue = 'anorexia')
plt.title('count plot to visualize anorexia in relation with Age')
plt.show()


# In[80]:


plt.figure(figsize=(15,6))
sns.countplot(x='age',data = hpts_data, hue = 'liver_big')
plt.title('count plot to visualize liver_big in relation with Age')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




