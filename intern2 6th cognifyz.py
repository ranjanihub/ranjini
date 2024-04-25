#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install folium')


# In[ ]:





# In[13]:


import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    'Name': ['Restaurant A', 'Restaurant B', 'Restaurant C'],
    'City': ['New York', 'Los Angeles', 'London'],
    'Latitude': [40.7128, 34.0522, 51.5074],
    'Longitude': [-74.0060, -118.2437, -0.1278],
    'Rating': [4.5, 3.8, 4.2]
}

df = pd.DataFrame(data)

m_basic = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=5)
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Name']).add_to(m_basic)



#Bar Chart
plt.figure(figsize=(10, 6))
sns.countplot(x='City', data=df)
plt.title('Number of Restaurants in Each City')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

#Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Rating', data=df)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.show()

#Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Latitude', y='Rating', data=df, s=100)
plt.title('Scatter Plot of Latitude vs. Rating')
plt.xlabel('Latitude')
plt.ylabel('Rating')
plt.show()


# In[15]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Name': ['Restaurant A', 'Restaurant B', 'Restaurant C'],
    'City': ['New York', 'Los Angeles', 'London'],
    'Latitude': [40.7128, 34.0522, 51.5074],
    'Longitude': [-74.0060, -118.2437, -0.1278],
    'Rating': [4.5, 3.8, 4.2]}
df = pd.DataFrame(data)


plt.figure(figsize=(8, 6))
sns.scatterplot(x='Latitude', y='Rating', data=df, s=100)
plt.title('Latitude vs. Rating for Restaurants')
plt.xlabel('Latitude')
plt.ylabel('Rating')
plt.grid(True)
plt.show()


# In[16]:


import pandas as pd
import folium

data = {
    'Name': ['Restaurant A', 'Restaurant B', 'Restaurant C'],
    'City': ['New York', 'Los Angeles', 'London'],
    'Latitude': [40.7128, 34.0522, 51.5074],
    'Longitude': [-74.0060, -118.2437, -0.1278],
    'Rating': [4.5, 3.8, 4.2]}
df = pd.DataFrame(data)

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=5)

for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Name']).add_to(m)

m.save('restaurant_map.html')

correlation = df['Latitude'].corr(df['Rating']) 
print("Correlation between Latitude and Rating:", correlation)


# In[ ]:





# In[ ]:




