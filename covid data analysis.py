#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


dataset=pd.read_csv(r"C:\Users\SONAL\Downloads\Covid\covid19_Confirmed_dataset.csv")


# In[6]:


dataset.head()


# In[7]:


dataset.shape


# In[8]:


#deleteing useless  lat and long columns
df=dataset.drop(["Lat","Long"],axis=1,inplace=True)


# In[9]:


dataset.head()


# In[10]:


#aggregate the rows by the country

corona_dataset_aggregated=dataset.groupby("Country/Region").sum()


# In[11]:


corona_dataset_aggregated.head()


# In[12]:


corona_dataset_aggregated.shape


# In[13]:


#visualise data
corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["India"].plot()
corona_dataset_aggregated.loc["Spain"].plot()

plt.legend()


# In[14]:


#calculating a good measure
corona_dataset_aggregated.loc["China"].plot()


# In[15]:


#calculate for first three days
corona_dataset_aggregated.loc["China"][:3].plot()


# In[16]:


#calculate the first derivative of the curve
corona_dataset_aggregated.loc["China"].diff().plot()


# In[17]:


#maximum infection rate
corona_dataset_aggregated.loc["China"].diff().max()


# In[18]:


corona_dataset_aggregated.loc["India"].diff().max()


# In[19]:


corona_dataset_aggregated.loc["Spain"].diff().max()


# In[20]:


countries=list(corona_dataset_aggregated.index)
max_infection_rates=[]

for c in countries:
     max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["Max_infected_rates"]=max_infection_rates


# In[21]:


corona_dataset_aggregated.head()


# In[22]:


#create a new dataframe
corona_data = pd.DataFrame(corona_dataset_aggregated["Max_infected_rates"])


# In[23]:


corona_data


# In[24]:


#importing the new dataset happiness_report
happiness_report = pd.read_csv(r"C:\Users\SONAL\Downloads\Covid\worldwide_happiness_report.csv")


# In[25]:


happiness_report


# In[26]:


#useless=['Overall rank','Score','Generosity','Perceptions of corruption']


# In[31]:


#happiness_report.drop("Overall rank",axis=1,inplace=True)
happiness_report.drop("Score",axis=1,inplace=True)
happiness_report.drop("Generosity",axis=1,inplace=True)
happiness_report.drop("Perceptions of corruption",axis=1,inplace=True)


# In[32]:


happiness_report.head()


# In[36]:


#happiness_report.set_index("Country or region",inplace=True)
happiness_report.head()


# In[37]:


corona_data.shape


# In[38]:


happiness_report.shape


# In[40]:


#joining data two datasets by inner join

data=corona_data.join(happiness_report,how="inner")
data


# In[41]:


#finding corelation
data.corr()


# In[43]:


x=data["GDP per capita"]
y=data["Max_infected_rates"]
sns.scatterplot(x,np.log(y))   #taking log values 


# In[44]:


sns.regplot(x,np.log(y))


# In[45]:


x=data["Social support"]
y=data["Max_infected_rates"]
sns.scatterplot(x,np.log(y))


# In[47]:


sns.regplot(x,np.log(y))


# In[48]:


x=data["Healthy life expectancy"]
y=data["Max_infected_rates"]
sns.scatterplot(x,np.log(y)) 


# In[49]:


sns.regplot(x,np.log(y))


# In[50]:


x=data["Freedom to make life choices"]
y=data["Max_infected_rates"]
sns.scatterplot(x,np.log(y)) 


# In[51]:


sns.regplot(x,np.log(y))


# In[ ]:




