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
def balanceLoad():
    x = 1
    for j in range(110):
        for i in range(50,1,-1):
            x *= i
            print(x)

    l = jsonify({'response':'success'})
    return l


if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)
