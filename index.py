## skafos-demo

# coding: utf-8

# ## Import the Skafos SDK

# In[1]:

import os
from skafossdk import *


# ## Instantiate the Skafos SDK

# In[2]:

skafos = Skafos()


# ## Create a Spark temp table from a Cassandra data source

# In[3]:

skafos.engine.create_view(
    "weather_table", 
    {"keyspace": "weather", "table": "weather_noaa"}, 
    DataSourceType.Cassandra).result()


# ## Select a subset of data from the Spark temp table

# In[4]:

weather = skafos.engine.query("SELECT * from weather_table where zipcode = '23250' limit 3").result()


# ## Execute your weather prediction model that outputs data like this

# In[5]:

data = [
    {"date": "2017-11-29", "temp_avg": 53, "temp_min": 35, "temp_max": 71},
    {"date": "2017-11-30", "temp_avg": 48, "temp_min": 36, "temp_max": 60},
    {"date": "2017-12-01", "temp_avg": 52, "temp_min": 39, "temp_max": 65}
] 


# ## Define schema of data to save

# In[6]:

schema = {
    "table_name":
    "my_weather_predictions",
    "options": {
        "primary_key": ["date"]
    },
    "columns": {
        "date": "date",
        "temp_avg": "float",
        "temp_min": "float",
        "temp_max": "float"
    }
}


# ## Save your model's results to your private keyspace

# In[7]:

dataresult = skafos.engine.save(schema, data).result()


# In[ ]:




