from flask import Flask, json, jsonify, redirect, request, url_for
from flask_pymongo import PyMongo
from bson import json_util
from flask_cors import CORS


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://worklao21:0881496697_Zaa@cluster0.b0htsww.mongodb.net/TaDee?retryWrites=true&w=majority"
mongo = PyMongo(app)
CORS(app)
database = mongo.db
collection = database['TaDee.chunks']

@app.route("/")
def home_page():
    return "<p>Hello</p>"


@app.route("/test")
def test_page():
    
    all_picture = collection.find()
    return json.loads(json_util.dumps(all_picture))


@app.route("/uploads/images/", methods=["POST"])
def save_upload():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    name =  request.args.get('name')
    data =  request.args.get('data')
    collection.insert_one({'name':name,'lat':lat,'lng':lng,'data':data})
    return json.loads(json_util.dumps(collection.find({'name':name})))

