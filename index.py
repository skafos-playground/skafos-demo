## skafos-demo

# coding: utf-8

## Import the Skafos SDK

import os
from skafossdk import *

## Instantiate the Skafos SDK

skafos = Skafos()

## Create a Spark temp table from a Cassandra data source

skafos.engine.create_view(
    "weather_table", 
    {"keyspace": "weather", "table": "weather_noaa"}, 
    DataSourceType.Cassandra).result()
print("Creating a spark temp view off of public weather data")
      
## Select a subset of data from the Spark temp table

weather = skafos.engine.query("SELECT * from weather_table where zipcode = '23250' limit 3").result()
print("Here's some of the weather data")
print(weather)

## Execute your weather prediction model that outputs data like this

data = [
    {"date": "2017-11-29", "temp_avg": 53, "temp_min": 35, "temp_max": 71},
    {"date": "2017-11-30", "temp_avg": 48, "temp_min": 36, "temp_max": 60},
    {"date": "2017-12-01", "temp_avg": 52, "temp_min": 39, "temp_max": 65}
] 

print("Here's my stubbed in weather prediction data")
print(data)

## Define schema of data to save

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

print("Here's the schema for my weather prediction data")

## Save your model's results to your private keyspace

dataresult = skafos.engine.save(schema, data).result()

print("Here's the result of my attempt to save my weather prediction data")
print(dataresult)
