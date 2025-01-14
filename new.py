import json
import csv
res = {}

contents = [
    'Seatle',
    'Cincinnati',
    'Maui',
    'San Diego'
]

#loop over all stations
for city_name in contents:  
    with open ('precipitation.json', 'r') as file:
        contents = json.load(file)


# Look into the all the various data' s
seatle_station = 'GHCND:US1WAKG0038' #Ensure that this is the correct code
seatle_data = []
Cincinnati_station = 'GHCND: USW00093814'
Cincinnati_data = []
Maui_station = 'GHCND:USC0051331'
San_Diego_station= 'GHCND:US1CASD0032'
Maui_data=  []
San_Diego_data = []

# assign the measurments per city 
for measurements in contents: 
    if measurements['station'] == seatle_station: 
        seatle_data.append(measurements)
    if measurements['station'] == Cincinnati_station:
        Cincinnati_data.append(measurements)
    if measurements['station'] == Maui_station:
        Maui_data = []
    if measurements['station'] == San_Diego_station:
        San_Diego_data.append(measurements)
        



#Seatle monthly precpitation: a list with the total precipitation per month

total_month_precipitation = {} # create a dictionary 

for measurements in contents: 
  month =  int(measurements['date'].split("-")[1]) #splitting the data to only get the months, which is in the second column, hence we are using 1
  if month in total_month_precipitation: #trying to get the sum of the seperate months
      total_month_precipitation[month] +=  measurements['value']
  else:
      total_month_precipitation[month] = 0
      
print(total_month_precipitation)

# Summing the precipitation values for each year
  
total_yearly_percipitation = sum(total_month_precipitation.values())

# The relative_monhtly_precipitation

relative_monthly_precipitation= {} 
# type: ignore
for month in total_month_precipitation:
    relative_monthly_precipitation[month] = (total_month_precipitation[month] / total_yearly_percipitation)
    
print(relative_monthly_precipitation)

#create a column of what will show up in the Jason file
res[city_name]=  {
    'month_precipitation' : total_month_precipitation,
    'year_precipitation' : total_yearly_percipitation, 
    'relative_precipitation' : relative_monthly_precipitation
            }    

# Create a Jason file 
with open('results.json', 'w') as file: 
    json.dump(res, file, indent = 20)







