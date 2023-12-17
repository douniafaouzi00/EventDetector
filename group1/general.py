from datetime import datetime 
from geopy.geocoders import Nominatim 
import pandas as pd
from math import radians, sin, cos, sqrt, atan2
import os
import glob
import json
from postget import Posts
from postget.exceptions.exceptions import *

def updateJson(alerts, type, start, end, startSlot, endSlot):
    for alert in alerts:        
        filepath = os.getcwd()+"/database.json"    
        if os.path.exists(filepath):
            new=True
            # Open the JSON file and read its contents
            with open(filepath, 'r') as f:
                data = json.load(f)
            results=data["results"]
            for result in results:
                if alert[0]==result["country"] and result["timeframe"]==[startSlot.strftime("%Y-%m-%d %H:%M:%S"), endSlot.strftime("%Y-%m-%d %H:%M:%S")] and result["type"]==type:    
                    new=False
                    # Update the desired field in the Python object
                    list = result['locations']
                    if not list.__contains__(alert[2]):
                        loc={}
                        loc["location"]=alert[2]
                        loc["timeframe"]=[start.strftime("%Y-%m-%d %H:%M:%S"),end.strftime("%Y-%m-%d %H:%M:%S")]
                        list.append(loc)
                    result['locations'] = list
            if new==True:
                event={}
                # add some data to the JSON file
                s=startSlot.strftime("%Y_%m_%dT%H_%M_%S")
                e=endSlot.strftime("%Y_%m_%dT%H_%M_%S")
                id=f"gr1-{alert[0]}-{s}-{e}-{type}"
                event["event_id"]=id
                event["country"]=alert[0]
                event["date"]=alert[1]
                event["type"]=type
                event["timeframe"]=[startSlot.strftime("%Y-%m-%d %H:%M:%S"),endSlot.strftime("%Y-%m-%d %H:%M:%S")]
                loc={}
                loc["location"]=alert[2]
                loc["timeframe"]=[start.strftime("%Y-%m-%d %H:%M:%S"),end.strftime("%Y-%m-%d %H:%M:%S")]
                event["locations"]=[loc]
                event["images"]=[]
                results.append(event)
            data["results"]=results
            # Convert the Python object back to JSON format
            updated_data = json.dumps(data)

            # Write the updated JSON string back to the file
            with open(os.getcwd()+"/database.json", 'w') as f:
                f.write(updated_data)
        else:
            data = {}
            # add some data to the JSON file
            s=startSlot.strftime("%Y_%m_%dT%H_%M_%S")
            e=endSlot.strftime("%Y_%m_%dT%H_%M_%S")
            id=f"gr1-{alert[0]}-{s}-{e}-{type}"
            data["event_id"]=id
            data["country"]=alert[0]
            data["date"]=alert[1]
            data["type"]=type
            data["timeframe"]=[startSlot.strftime("%Y-%m-%d %H:%M:%S"),endSlot.strftime("%Y-%m-%d %H:%M:%S")]
            loc={}
            loc["location"]=alert[2]
            loc["timeframe"]=[start.strftime("%Y-%m-%d %H:%M:%S"),end.strftime("%Y-%m-%d %H:%M:%S")]
            data["locations"]=[loc]
            data["images"]=[]
            result={}    
            result["results"] = [data]
            #open the same JSON file for writing
            with open(os.getcwd()+"/database.json", 'w') as file:
                json.dump(result, file)
            
def appendImages(start,end, startSlot,endSlot, twitter_getter: Posts):
    start_time = int(start.timestamp())
    end_time = int(end.timestamp())
    print(start_time, end_time)
    file_path = os.getcwd()+"/database.json"
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r') as file:
        data = json.load(file)
    results=data["results"]
    for result in results:
        country=result["country"]
        locations=result["locations"]
        imgs=result["images"]
        type=result["type"]
        timeframe=result["timeframe"]
        if [startSlot.strftime("%Y-%m-%d %H:%M:%S"),endSlot.strftime("%Y-%m-%d %H:%M:%S")]==timeframe:
            tweets=[]
            #tweet for country
            twitter_getter.go_home()
            twitter_getter.set_num_scrolls(10)
            twitter_getter.set_query(f'#{type} #{country} #damage')
            print(f'start: {start_time} end: {end_time}')
            twitter_getter.set_since_time(str(start_time))
            twitter_getter.set_until_time(str(end_time))
            
            try:
                twitter_getter.search()
            except ElementNotLoaded as e:
                raise e
            except NoTweetsReturned as e:
                print(e)
            
            #tweet for country second search, no hashtag
            twitter_getter.go_home()
            twitter_getter.set_query(f'{type} {country}')
            print(f'start: {start_time} end: {end_time}')
            twitter_getter.set_since_time(str(start_time))
            twitter_getter.set_until_time(str(end_time))

            try:
                twitter_getter.search()
            except ElementNotLoaded as e:
                raise e
            except NoTweetsReturned as e:
                print(e)

            #tweet for country third search, country is hashtag
            twitter_getter.go_home()
            twitter_getter.set_query(f'{type} #{country}')
            print(f'start: {start_time} end: {end_time}')
            twitter_getter.set_since_time(str(start_time))
            twitter_getter.set_until_time(str(end_time))

            try:
                twitter_getter.search()
            except ElementNotLoaded as e:
                raise e
            except NoTweetsReturned as e:
                print(e)

            #tweet for country fourth search, event type is hashtag
            twitter_getter.go_home()
            twitter_getter.set_query(f'#{type} {country}')
            print(f'start: {start_time} end: {end_time}')
            twitter_getter.set_since_time(str(start_time))
            twitter_getter.set_until_time(str(end_time))
            
            try:
                twitter_getter.search()
            except ElementNotLoaded as e:
                raise e
            except NoTweetsReturned as e:
                print(e)
            
            #tweet for city
            twitter_getter.set_num_scrolls(2)
            cities = getNearCity(locations[0]["location"][0],locations[0]["location"][1])
            for city in cities:
                twitter_getter.go_home()
                twitter_getter.set_query(f'#{type} {city} #damage')
                
                try:
                    twitter_getter.search()
                except ElementNotLoaded as e:
                    raise e
                except NoTweetsReturned as e:
                    print(e)
                
            tweets = twitter_getter.get_tweets_data()
            twitter_getter.print_results()
            twitter_getter.clear_tweets()
            #cleartweet
            for tweet in tweets:
                discussion_link = tweets[tweet]['discussion_link']
                images_list = tweets[tweet]['images']
                video_preview_list = tweets[tweet]['video_preview']
                date = tweets[tweet]['datetime_timestamp']
                for i in images_list:
                    image={}
                    image["tweet_url"]=discussion_link
                    image["image_url"]=i
                    image["date"]=date
                    image["timeframe"]=[start.strftime("%Y-%m-%d %H:%M:%S"), end.strftime("%Y-%m-%d %H:%M:%S")]
                    if not imgs.__contains__(image):
                        imgs.append(image)
                for v in video_preview_list:
                    image={}
                    image["tweet_url"]=discussion_link
                    image["image_url"]=v
                    image["date"]=date
                    image["timeframe"]=[start.strftime("%Y-%m-%d %H:%M:%S"), end.strftime("%Y-%m-%d %H:%M:%S")]
                    if not imgs.__contains__(image):
                        imgs.append(image)
            result["images"]=imgs
        data["results"]=results
        updated_data = json.dumps(data)
        with open(file_path, 'w') as f:
            f.write(updated_data)

def getNearCity(lat,lon):
    cities=[]
    
    # Load the city data into a pandas DataFrame
    city_data = pd.read_csv('FindingCitiesNearTag/worldcities.csv')
    
    # Define the radius of the area of interest in kilometers (can be adjusted according to the entity of the event)
    radius = 100

    # Define the number of nearest cities to retrieve (can be adjusted according to the entity of the event)
    num_nearest_cities = 1
    
    # Calculate the distances between the target coordinates and the coordinates of all the cities in the list
    city_data['distance'] = city_data.apply(lambda row: calc_distance(lat, lon, row['lat'], row['lng']), axis=1)

    # Filter the cities within the specified radius
    nearby_cities = city_data[city_data['distance'] <= radius]

    # Sort the cities by their distance from the target
    nearby_cities = nearby_cities.sort_values(by='distance')
    # Retrieve the nearest cities
    nearest_cities = nearby_cities.head(num_nearest_cities)
    # Display the nearest citie
    for city in nearest_cities['city_ascii']:
        cities.append(city)
    return cities

# Define a function to calculate the distance between two points on the Earth's surface using the Haversine formula
def calc_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance