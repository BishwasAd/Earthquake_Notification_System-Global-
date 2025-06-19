from flask import Flask, jsonify
import requests
import send
import threading
import time

app = Flask(__name__)
#it avoids duplicate sms sending
sent = set()

#url for love feed of earthquake data
feed_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
#time ben each pollling
time_interval = 60
#goes through all feeds from url
def quake_data():
    while True:
        try:
            print("Checking for new data")
            response= requests.get(feed_url)
            data= response.json()
            events= data.get("features",[])
            print(f"Found {len(events)} event feeds")

            for event in events:
                event_id= event.get("id")
                # avoids same feed to be processed
                if event_id in sent:
                    continue
                # Get info about the earthquake
                properties = event.get("properties",{})
                title = properties.get("title", "Earthquake Alert!!!")
                url = properties.get("url", "")
                # message to send in sms
                message= f"Earthquake Alert!\n{title}\n{url}"
                # send.py handles actual sending_   calls the function send_sms
                send.send_sms(message)
                # adds event_id to sent_ids for further future loops
                sent.add(event_id)
                print(f"Alert sent for event:{event_id}")
            print('Done checking\n')
    
        except Exception as e:
            print(f"something went wrong: {e}")
        #Wait beforing polling again
        time.sleep(time_interval)

@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "poll_interval_seconds": time_interval,
        "feed_url": feed_url
    })

if __name__ == "__main__":
    #srarts bg polling thread
    polling_thread= threading.Thread(target= quake_data)
    polling_thread.daemon = True
    polling_thread.start()

    app.run(debug=True)