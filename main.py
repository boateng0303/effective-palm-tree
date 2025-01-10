# find where the ISS is located

from get_iss import iss_loc
from get_weather import get_weather
from get_distance import dist
from get_reverse_geo import address
from get_country import country



data= iss_loc()
lat,lon =  data[0],data[1]


#weather
weather = get_weather(lat,lon)

temp_c = round(weather["main"]["temp"]- 284.2,2)
description = weather["weather"][0]["description"]
print(str(temp_c),"C",description)




# Reverse geolocation
add = address(lat,lon)




# Print the country code
print("Country Code is :",add["countryCode"])
name= add["countryCode"]

if(add["countryCode"]==""):
    print("The ISS is over water!")
else:
    location = add["countryCode"]
    print(add["countryCode"])
    flag = country(location)[0]["flags"]["png"]
    print(flag)







#distance between ISS and myself
distance= dist(lat,lon,46.5193586,-80.9763077)

print(f"I am {distance} awy from ISS in km!")



