from flask import Flask, json, jsonify, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://worklao21:0881496697_Zaa@cluster0.b0htsww.mongodb.net/TaDee?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    database = mongo.db
    all_picture = database['TaDee.chunks'].find()
    
    return jsonify(list(all_picture))
@app.route("/uploads/<path:filename>", methods=["POST"])
def save_upload(filename):
    mongo.save_file(filename, request.files["file"])
    return redirect(url_for("TaDee", filename=filename))