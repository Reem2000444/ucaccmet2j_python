import json
import csv
res = {}
with open ('stations.csv',) as file: 
    stations = list(csv.DictReader(file))
with open ('precipitation.json', 'r') as file:
        contents = json.load(file)

#finding all the data for the various statiosn
for station in stations: 
    #city_date
    station_number = station['Station']
    state = station['State']
    city_name = station['Location']

    station_data=[]
    for measurements in contents: 
        if measurements['station'] == station['Station']: 
            station_data.append(measurements)

    #Seatle monthly precpitation: a list with the total precipitation per month

    total_month_precipitation = {} # create a dictionary 

    for measurements in station_data: 
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
    json.dump(res, file, indent = 4)







