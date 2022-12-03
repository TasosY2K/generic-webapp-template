import requests
import paho.mqtt.client as mqtt
import datetime
import time
username_format="teamA-fog1"
instance="1"

password="fL98E"
host_http="pegasus.csd.auth.gr"
host_mqtt=host_http

offset=5
window_width=60

client = mqtt.Client()
client.username_pw_set(username_format,password)
client.connect(host_mqtt,1883,60)
#print(client)
#def get_data():
        #yield msg
          

while True:
    json_template={"metricID":["Voltage"],"from":datetime.datetime.now().timestamp()-window_width}
    r=requests.post(f"http://{host_http}:50000/get",json=json_template)
    timedata=r.json()["monitoring"][0]["data"][0]["values"]
    for data in timedata:
        msg=str(data["timestamp"])+","+str(data["val"])
        #print(msg)
        client.publish(topic="teamA/fog1/dev",qos=1,payload=msg)
    client.loop_write()
    #time.sleep(offset)
