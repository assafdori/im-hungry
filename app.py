from flask import Flask, jsonify
import requests
import time
import json

app = Flask(__name__)

def check_venue_status():
    api_url = "https://consumer-api.wolt.com/order-xp/web/v1/venue/slug/hamosad/dynamic/"
    try:
        response = requests.get(api_url, verify=False)
        print("-----------debugger start---------------")
        print(response.json()["venue"]["delivery_open_status"]["is_open"])
        data = response.json()["venue"]["delivery_open_status"]
        return data["is_open"]
    except Exception as e:
        print(f"Error: {e}")
        return False

@app.route("/")
def index():
    return jsonify({"is_open": check_venue_status()})

if __name__ == "__main__":
    app.run(debug=True, port=8080)

