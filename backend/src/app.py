# load libaries
from flask import Flask, jsonify
import sys
import json
from src.api_spec import spec
from sqlalchemy import Column, Integer, Float, String, TIMESTAMP, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class PowerMeasurement(Base):
    __tablename__ = "PowerMeasurement"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    source = Column(String)
    value = Column(String)

    def __dict__(self):
        return {'id': self.id, 'timestamp': self.timestamp, 'source': self.source, 'value': self.value}

# load modules
app = Flask(__name__)
DB_PATH = "postgresql://postgres:root@localhost:5432/postgres"
engine = create_engine(DB_PATH, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/get")
def get_data():
    sql = text("SELECT * FROM PowerMeasurement")
    data = engine.execute(sql)
    print(data)
    f = []
    for i in data:
        f.append(dict(i))
    return jsonify(f)