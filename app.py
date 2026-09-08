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
