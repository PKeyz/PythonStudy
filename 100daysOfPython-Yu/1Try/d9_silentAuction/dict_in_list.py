travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the Code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(countryName, visitsNum, citiesList):
    new_country_dict = dict([("country", countryName),("visits", visitsNum),( "cities", citiesList)])
    travel_log.append(new_country_dict)



#🚨 Do not change the Code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
