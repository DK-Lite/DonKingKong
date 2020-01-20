import json
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

def change_key(dic, key, value):
    dic[key]=value
    return dic

@app.route("/", methods=["GET"])
def StartPage():
    return 'hello'

@app.route("/data-lake/apt-trade-info", methods=['POST'])
def PostDataLake():
    client = MongoClient("localhost", 17017)
    db = client.data_lake
    collection = db.apt_trade_info
    collection.insert(request.form.to_dict())
    client.close()
    return "Success!!"

@app.route("/data-lake/apt-trade-info", methods=['GET'])
def GetDataLake():
    client = MongoClient("localhost", 17017)
    db = client.data_lake
    collection = db.apt_trade_info
    cursor = collection.find()
    docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]
    client.close()
    return { 'info': docs }

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port='3691')