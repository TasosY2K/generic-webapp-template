import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import paho.mqtt.client as mqtt
from models import PowerMeasurement
from datetime import datetime

engine = db.create_engine("postgresql://postgres:root@localhost:5432")

broker_url = "pegasus.csd.auth.gr"
broker_port = 1883

username = "teamA-cloud"
password = "fL98E"

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# functions
def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code: {}".format(rc))

def on_disconnect(client, userdata, rc):
   print("Client Got Disconnected")

def on_message(client, userdata, message):
   t, v = message.payload.decode().split(",") # timestamp,value
   pm = PowerMeasurement()
   pm.timestamp = t
   pm.value = v
   pm.source = "FOG1"
   db.add(pm)
   db.commit()

   # print("Message Recieved: "+message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)
client.connect(broker_url, broker_port)

client.subscribe(topic="teamA/fog1/dev", qos=1)

client.loop_forever()