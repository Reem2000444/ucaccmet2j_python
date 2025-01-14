import json
import csv
res = {}

#open both of the files
with open ('stations.csv',) as file: 
    stations = list(csv.DictReader(file))
with open ('precipitation.json', 'r') as file:
        contents = json.load(file)


total_precipitation_all_stations = 0 #start with 0!

#loop for all the data for the various stations
for station in stations: 
    station_number = station['Station']
    state = station['State']
    city_name = station['Location']

    #Now find all the data per station
    station_data=[] 
    for measurements in contents: 
        if measurements['station'] == station['Station']: 
            station_data.append(measurements)

    #Seatle monthly precpitation: a list with the total precipitation per month

    total_month_precipitation = {} # create a dictionary to store all information

    for measurements in station_data: 
        month =  int(measurements['date'].split("-")[1]) #splitting the data to only get the months, which is in the second column, hence we are using 1
        if month in total_month_precipitation: #trying to get the sum of the seperate months
            total_month_precipitation[month] +=  measurements['value'] #add all the value of the specific month it'll loop over
        else:
            total_month_precipitation[month] = 0#enter the month if not already in the dictionary

    # Summing the precipitation values for each year
    total_yearly_percipitation = sum(total_month_precipitation.values())

    # The relative_monhtly_precipitation per month over the entire year per city (still inside the loop)
    relative_monthly_precipitation= {} #dictionary for the relative monthly precipitation
    for month in total_month_precipitation:
        relative_monthly_precipitation[month] = (total_month_precipitation[month] / total_yearly_percipitation)
        
   
 #create the information what will show up in the Jason file
    res[city_name]=  {
        'month_precipitation' : total_month_precipitation,
        'year_precipitation' : total_yearly_percipitation, 
        'relative_precipitation' : relative_monthly_precipitation
                }    

    #summing the precipitation values for each year
    total_yearly_precipitation = sum(total_month_precipitation.values())

    # add to the global total precipitation
    total_precipitation_all_stations += total_yearly_precipitation 

for city_name, data in res.items():
    data['relative_yearly_precipitation'] = (
        data['total_yearly_precipitation']/ total_precipitation_all_stations)
    
     


# Create the Jason file 
with open('results.json', 'w') as file: 
    json.dump(res, file, indent = 4)







