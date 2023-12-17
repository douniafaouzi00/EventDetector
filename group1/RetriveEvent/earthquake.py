from datetime import datetime
from geopy.geocoders import Nominatim 
import requests
import json
    
def getAlerts(start, end, magnitude, eventType):
    print(start,end)
    #apiCall

    apiCall="https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime="+start.strftime("%Y-%m-%dT%H:%M:%S")+"&endtime=" + end.strftime("%Y-%m-%dT%H:%M:%S") +"&minmagnitude="+str(magnitude)+"&eventtype="+eventType+"&orderby=time-asc"
    response = requests.get(apiCall)
    json_data=json.loads(response.text)

    #filter json result to retrive only relevant event
    list = getData(json_data)
    return list
    
#filter json data to evaluate only relevant events
def getData(json_data):
    list=[]
    for obj in json_data.get("features"):
        prop = obj.get("properties")
        time=prop.get("time")
        geom = obj.get("geometry")
        coordinate=geom.get("coordinates")
        lat, lon = (coordinate[0],coordinate[1])
        datetime_utc = datetime.utcfromtimestamp(time/1e3).strftime('%Y-%m-%d %H:%M:%S')
        if -90<= lat <= 90 and -90 <= lon <= 90 :
            #get country
            country = getCountry(lat,lon)
            if(country!=""):
                #add alert
                list.append([country,datetime_utc,[lat,lon]])
    return list
        
#get country given the latitude and longitude
def getCountry(latitude, longitude):
    # Initialize geolocator
    geolocator = Nominatim(user_agent="my_app")

    # Find the location corresponding to the given latitude and longitude
    location = geolocator.reverse(f"{latitude}, {longitude}")
    #json_string = json.dumps(location.raw, indent=4)

    # Print the JSON string with pretty formatting using prettyjson
        # use the reverse() method of the geocoder to get the location information
    location = geolocator.reverse((latitude, longitude), exactly_one=True, language='en')    
    # extract the country from the location object
    return location.raw['address'].get('country', '')



    

