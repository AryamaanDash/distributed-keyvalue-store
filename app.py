import os
import time

from flask import Flask, request, jsonify
import requests as http_requests

app = Flask(__name__)

#in-memory key-value store
store = {}

#configurations from environment
NODE_NAME = os.environ.get("NODE_NAME", "node1")
PEERS = [p for p in os.environ.get("PEERS", "").split(",") if p]
MODE = os.environ.get("MODE", "CP")

# NODE_NAME, PEERS, and MODE are pulled from environment variables so each container can have its own identity and know where its peers live. 
#Docker Compose will inject these values later.

#GET, POST, PATCH, PUT, DELETE are the primary HTTP methods used to perform CRUD(Create, Read, Update, Delete) operations in RESTful web APIs.
#GET is read
#POST is to create
#PUT is for update/replace with full source replacement
#PATCH is for update with partial resource modification
#DELETE is for resource removal

@app.route("/data", methods=["GET"])
def get_all_data():
    return jsonify({"node": NODE_NAME, "mode": MODE, "store": store})

@app.route("/data/<key>", methods=["GET"])
def get_data(key):
    if key in store:
        return jsonify({"node": NODE_NAME, "key": key, "value": store[key]})
    return jsonify({"error": "Key not found"}), 404

