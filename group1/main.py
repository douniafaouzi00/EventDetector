import pytz
import yaml
from  RetriveEvent import earthquake
import general
from datetime import datetime, timedelta
from postget.Posts import Posts
from postget.exceptions.exceptions import *
import os

def main():
    file_path = os.getcwd()+"/database.json"
    # Check if the path is a file or directory
    if os.path.isfile(file_path):
        # Delete the file
        os.remove(file_path)

    twitter_getter = Posts(username='', password='', email_address='', query='', num_scrolls=2, mode=1, wait_scroll_base = 5, wait_scroll_epsilon = 2, headless=True)
    try:
        twitter_getter.login()
    except ElementNotLoaded as e:
        raise e
    with open('parameters.yaml', 'r') as f:
       data = yaml.safe_load(f)

    # test query to see if works
    twitter_getter.set_query('test')
    twitter_getter.search()
    twitter_getter.set_query('')
    twitter_getter.go_home()
    twitter_getter.clear_tweets()

    magnitude = data['magnitude']
    eventType = data['eventType']
    iterationTime = data['iterationTime']
    timeframe = data['timeframe']
    start=datetime.strptime(data['simDate'], '%Y-%m-%d')
    start=pytz.timezone('UTC').localize(start)
    startSlot=start
    num=((24*60)/iterationTime)/timeframe
    print(num)
    print(timeframe)
    for _ in range(0, timeframe):
        endSlot=startSlot+timedelta(hours=24/timeframe)
        for i in range(0,int(num)):
            print("Iteration "+str(i))
            end = start + timedelta(minutes=iterationTime)
            #getAlert between start and end and with fitted requirement of magnitude and type
            alerts= earthquake.getAlerts(start,end, magnitude, eventType)
            #update and create json file with events
            general.updateJson(alerts,eventType,start,end,startSlot,endSlot)  
            #get images for each event json file
            general.appendImages(start,end, startSlot,endSlot, twitter_getter) 
            start = end
        
        startSlot=endSlot
        #send file group 3?
    twitter_getter.quit_browser()
            
            
    
if __name__=='__main__':
    main()