from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from config import Config
from datetime import datetime
from functools import wraps

API_KEY = "PlanItIsTheBestProjectEverXYZ"

app = Flask(__name__)
app.config.from_object(Config)
client = MongoClient(app.config['MONGO_URI'])

CORS(app)
db = client.wad2
collection = db.routes

# API Key


def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if api_key and api_key == API_KEY:
            return f(*args, **kwargs)
        else:
            return jsonify({"message": "Invalid or missing API key."}), 403
    return decorated


# Healthcheck


@app.route("/")
@require_api_key
def health_check():
    return jsonify(
        {
            "message": "Service is healthy."
        }
    ), 200


# Database healthcheck


@app.route("/db")
@require_api_key
def db_check():
    client = MongoClient('localhost', serverSelectionTimeoutMS=1000)
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        return jsonify({"message": "Database is healthy."}), 200
    except ServerSelectionTimeoutError:
        return jsonify({"message": "Database is unhealthy."}), 500

# Create (POST)


@app.route("/routes", methods=['POST'])
@require_api_key
def create_route():
    data = request.json
    data['timestamp'] = datetime.now()
    collection.insert_one(data)
    return jsonify({"message": "Route created successfully."}), 201

# Read All (GET)


@app.route("/routes", methods=['GET'])
@require_api_key
def read_all_routes():
    all_routes = list(collection.find())
    for route in all_routes:
        route["_id"] = str(route["_id"])
    return jsonify(all_routes), 200

# Read All EMAIL OF USER(GET)


@app.route("/routes/email", methods=['GET'])
@require_api_key
def read_all_routes_email():
    email = request.args.get('email')
    if email:
        all_routes = list(collection.find({"user_id": email}))
        for route in all_routes:
            route["_id"] = str(route["_id"])
        return jsonify(all_routes), 200
    else:
        return jsonify({"message": "Email parameter is required."}), 400

# Read One (GET)


@app.route("/routes/<route_id>", methods=['GET'])
@require_api_key
def read_one_route(route_id):
    route = collection.find_one({"route_id": route_id})
    if route:
        route["_id"] = str(route["_id"])
        return jsonify(route), 200
    else:
        return jsonify({"message": "Route not found."}), 404

# Update (PUT)


@app.route("/routes/<route_id>", methods=['PUT'])
@require_api_key
def update_route(route_id):
    data = request.json
    updated_route = collection.find_one_and_update(
        {"route_id": route_id}, {"$set": data})
    if updated_route:
        return jsonify({"message": "Route updated successfully."}), 200
    else:
        return jsonify({"message": "Route not found."}), 404

# Delete (DELETE)


@app.route("/routes/<route_id>", methods=['DELETE'])
@require_api_key
def delete_route(route_id):
    deleted_route = collection.find_one_and_delete({"route_id": route_id})
    if deleted_route:
        return jsonify({"message": "Route deleted successfully."}), 200
    else:
        return jsonify({"message": "Route not found."}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)  # must be same as gunicorn
