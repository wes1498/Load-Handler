#!/usr/bin/python3
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps



import getpass
import sys
import time


app = Flask(__name__)
api = Api(app)



@app.route("/")
def home():
    return render_template("index.html")

@app.route('/loadBalancer', methods=['GET'])
# @app.route("/")
def autopass():
    return render_template("success.html")



if __name__ == '__main__':
     app.run(debug=True)
