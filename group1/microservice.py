#import datetime
from datetime import datetime, timedelta, time
import glob
import json
import os
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/debug')
def serve_file():
    file_path = os.getcwd()+"/database.json"
    if os.path.exists(file_path):
        return send_from_directory(os.getcwd(), "database.json")
    else:
        return "No file found"
    
@app.route('/twitterevents',methods=['POST'])
def serve_tweet():
    group2 = request.get_json()
    file_path = os.getcwd()+"/database.json"
    response={}
    if not os.path.exists(file_path):
        response["results"] = group2["results"]
        return response
    start = datetime.strptime(group2.get('start'), '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(group2.get('end'), '%Y-%m-%d %H:%M:%S')
    startD = time(hour=0, minute=0, second=0)
    midD= time(hour=12, minute=0, second=0)
    endD = time(hour=23, minute=59, second=59)
    if startD < start.time() < midD:
        slot = [startD, midD]
    else:
        slot = [midD, endD]
    events=[]
    with open(file_path, 'r') as file:
        data = json.load(file)
    results=data["results"]
    print("Crawling for alerts from source... ")
    for result in results:
        date=datetime.strptime(result["date"],'%Y-%m-%d %H:%M:%S')
        if slot[0]<date.time()<slot[1]:
            if(start<=date<=end):
                print("Alert found")
                print("Creating alert:")
                event={}
                event["event_id"]=result["event_id"]
                event["country"]=result["country"]
                event["date"]=result["date"]
                event["type"]=result["type"]
                event["timeframe"]=result["timeframe"]
                print("event: "+event["type"]+ " in "+ event["country"])
                locations=result["locations"]
                list=[]
                for location in locations:
                    if datetime.strptime(location["timeframe"][0],'%Y-%m-%d %H:%M:%S')<end:
                        list.append(location["location"])
                event["locations"]=list
                imgs=result["images"]
                images=[]
                print("Retrive images from twitter")
                for image in imgs:
                    if datetime.strptime(image["date"],'%Y-%m-%d %H:%M:%S')<end:
                        images.append(image)
                event["images"]=images
                events.append(event)
            else:
                if(date < end): 
                    event={}
                    event["event_id"]=result["event_id"]
                    event["country"]=result["country"]
                    event["date"]=result["date"]
                    event["type"]=result["type"]
                    event["timeframe"]=result["timeframe"]
                    locations=result["locations"]
                    list=[]
                    for location in locations:
                        if datetime.strptime(location["timeframe"][0],'%Y-%m-%d %H:%M:%S')<end:
                            if datetime.strptime(location["timeframe"][0],'%Y-%m-%d %H:%M:%S')<end:
                                print("New alert on event: "+event["type"]+" in "+event["country"]+ " new location added.")
                            list.append(location["location"])
                    event["locations"]=list
                    imgs=result["images"]
                    images=[]
                    print("Retrive images from twitter")
                    for image in imgs:
                        if datetime.strptime(image["date"],'%Y-%m-%d %H:%M:%S')<end:
                            images.append(image)
                    event["images"]=images
                    events.append(event)
    
    print("Merge event with group2")
    g2results=group2.get('results')
    if(g2results==[]):
        print("No event from group2")
    else:
        for g2result in g2results:
            g2country= g2result["country"]
            g2timeframe= g2result["timeframe"]
            g2type= g2result["type"]
            g2locations=g2result["locations"]
            g2images= g2result["images"]
            found=False
            for event in events:
                if event["country"]==g2country and event["timeframe"]==g2timeframe and event["type"]==g2type:
                    print("Event matched adding location and images...")
                    found=True
                    g1locations=event["locations"]
                    for g2location in g2locations:
                        if not g1locations.__contains__(g2location):
                            g1locations.append(g2location)
                    g1images=event["images"]
                    for g2image in g2images:
                        if not g1images.__contains__(g1images):     
                            g1images.append(g2images)
                    event["locations"]=g1locations
                    event["images"]=g1images
            if found==False:
                print("Different event found, adding to list of events")
                events.append(g2result)
    response["results"]=events
    return response
            
            

if __name__ == '__main__':
    app.run(port=1111, host='0.0.0.0')
    