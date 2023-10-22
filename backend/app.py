from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from pymongo import MongoClient, ReturnDocument
from pymongo.errors import ServerSelectionTimeoutError
from config import Config
from datetime import datetime
from functools import wraps
from bson import ObjectId

app = Flask(__name__)
app.config.from_object(Config)
client = MongoClient(app.config['MONGO_URI'])
API_KEY = "PlanItIsTheBestProjectEverXYZ"
db = client.wad2
collection = db.routes
user_collection = db.users

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, x-api-key')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH')
    return response

# HELPER FUNCTIONS
def convert_objectid_to_string(data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = convert_objectid_to_string(value)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            data[index] = convert_objectid_to_string(item)
    elif isinstance(data, ObjectId):
        return str(data)
    return data


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
def get_all_routes():
    routes = [str(rule) for rule in app.url_map.iter_rules()]
    return jsonify({"routes": routes}), 200


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

# CRUD Operations

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

# User Operations

# Update or create user init into our backend, since we're using auth0
@app.route("/users", methods=['POST'])
@require_api_key
def create_or_update_user():
    """
    This function handles the POST request at the /users endpoint.
    It either creates a new user or updates an existing user based on the provided auth0_user_id.
    If the auth0_user_id and email are not provided in the request, it returns a 400 error with a message.
    If the user already exists, it updates the user's data and returns a 200 status code with a success message and the updated user data.
    If the user does not exist, it creates a new user with the provided data, current timestamp, and empty friends and friendRequests lists, and returns a 201 status code with a success message.
    """
    data = request.json
    auth0_user_id = data.get('auth0_user_id')
    email = data.get('email')
    if not auth0_user_id or not email:
        return jsonify({"message": "Both auth0_user_id and email are required."}), 400
    existing_user = user_collection.find_one({"auth0_user_id": auth0_user_id})
    if existing_user:
        updated_user = user_collection.find_one_and_update(
            {"auth0_user_id": auth0_user_id}, {"$set": data}, return_document=ReturnDocument.AFTER)
        if updated_user:
            updated_user["_id"] = str(updated_user["_id"])
            return jsonify({"message": "User updated successfully.", "user": updated_user}), 200
    else:
        data['timestamp'] = datetime.now()
        data['friends'] = []
        data['friendRequests'] = {"sent": [], "received": []}
        user_collection.insert_one(data)
        return jsonify({"message": "User created successfully."}), 201

# Users get individual user
@app.route("/users/<user_email>", methods=['GET'])
@require_api_key
def get_user(user_email):
    """
    This function handles the GET request at the /users/<user_email> endpoint.
    It retrieves the user with the given email.
    If the user is found, it returns a JSON object containing the user data.
    If the user is not found, it returns a 404 error with a message.
    """
    user = user_collection.find_one({"email": user_email})
    if user:
        user = convert_objectid_to_string(user)
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found."}), 404


# Friend Requests Backend Calls
@app.route("/users/<user_email>/friend_requests", methods=['GET'])
@require_api_key
def get_friend_requests(user_email):
    """
    This function handles the GET request at the /users/<user_email>/friend_requests endpoint.
    It retrieves the friend requests of a user with the given email.
    If the user is found, it returns a JSON object containing the friend requests.
    If the user is not found, it returns a 404 error with a message.
    """
    # Find the user in the database using the provided email
    user = user_collection.find_one({"email": user_email})
    if user:
        friend_requests = user.get('friendRequests', {})
        friend_requests.setdefault('sent', [])
        friend_requests.setdefault('received', [])
        # Convert ObjectId to string
        friend_requests['sent'] = [str(request_id) for request_id in friend_requests['sent']]
        friend_requests['received'] = [
            str(request_id) for request_id in friend_requests['received']]
        return jsonify(friend_requests), 200
    else:
        # If the user is not found, return a 404 error with a message
        return jsonify({"message": "User not_found."}), 404
    

# Friend Request Send
@app.route("/users/<user_email>/friend_requests/send", methods=['POST'])
@require_api_key
def send_friend_request(user_email):
    """
    This function handles the POST request at the /users/<user_email>/friend_requests/send endpoint.
    It sends a friend request from the current user to the user with the given email.
    If both users are found, it adds the friend request to the current user's friendRequests.sent list
    and the receiving user's friendRequests.received list.
    If any user is not found, it returns a 404 error with a message.
    """
    # Find the current user in the database using the provided email
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        # Get the email of the user to send the friend request to
        friend_email = request.json.get('friend_email')
        # Check if the friend request has already been sent
        if friend_email in current_user['friendRequests']['sent']:
            return jsonify({"message": "Friend request already sent."}), 400
        # Find the user to send the friend request to in the database
        friend_user = user_collection.find_one({"email": friend_email})
        if friend_user:
            # Add the friend request to the current user's friendRequests.sent list
            current_user['friendRequests']['sent'].append(friend_email)
            user_collection.update_one({"email": user_email}, {"$set": current_user})

            # Add the friend request to the receiving user's friendRequests.received list
            friend_user['friendRequests']['received'].append(user_email)
            user_collection.update_one({"email": friend_email}, {"$set": friend_user})

            return jsonify({"message": "Friend request sent successfully."}), 200
        else:
            # If the user to send the friend request to is not found, return a 404 error with a message
            return jsonify({"message": "Friend not found."}), 404
    else:
        # If the current user is not found, return a 404 error with a message
        return jsonify({"message": "User not found."}), 404
    

# Friend Request Decline
@app.route("/users/<user_email>/friend_requests/decline", methods=['POST'])
@require_api_key
def decline_friend_request(user_email):
    """
    This function handles the POST request at the /users/<user_email>/friend_requests/decline endpoint.
    It declines a friend request from the current user to the user with the given email.
    If the user is found, it removes the friend request from the user's friendRequests.received list.
    If the user is not found, it returns a 404 error with a message.
    """
    # Find the current user in the database using the provided email
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        # Get the email of the user to decline the friend request from
        friend_email = request.json.get('friend_email')
        # Find the user to decline the friend request from in the database
        friend_user = user_collection.find_one({"email": friend_email})
        if friend_user:
            # Check if the friend request has already been declined
            if user_email not in friend_user['friendRequests']['sent']:
                return jsonify({"message": "Friend request already declined or not found."}), 400
            # Remove the friend request from the user's friendRequests.received list
            friend_user['friendRequests']['sent'].remove(user_email)
            user_collection.update_one({"email": friend_email}, {"$set": friend_user})

            # Also remove the friend request from the current user's friendRequests.sent list
            current_user['friendRequests']['received'].remove(friend_email)
            user_collection.update_one({"email": user_email}, {"$set": current_user})

            return jsonify({"message": "Friend request declined successfully."}), 200
        else:
            # If the user to decline the friend request from is not found, return a 404 error with a message
            return jsonify({"message": "Friend not found."}), 500
    else:
        # If the current user is not found, return a 404 error with a message
        return jsonify({"message": "User not found."}), 404

# Friend Request Accept
@app.route("/users/<user_email>/friend_requests/accept", methods=['POST'])
@require_api_key
def accept_friend_request(user_email):
    """
    This function handles the POST request at the /users/<user_email>/friend_requests/accept endpoint.
    It accepts a friend request from the current user to the user with the given email.
    If the user is found, it adds the current user to the user's friends list and removes the friend request
    from the user's friendRequests.received list.
    If the user is not found, it returns a 404 error with a message.
    """
    # Find the current user in the database using the provided email
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        # Get the email of the user to accept the friend request from
        friend_email = request.json.get('friend_email')
        # Find the user to accept the friend request from in the database
        friend_user = user_collection.find_one({"email": friend_email})
        if friend_user:
            # Check if the friend request has already been accepted or does not exist
            if user_email not in friend_user['friendRequests']['sent']:
                return jsonify({"message": "Friend request already accepted or not found."}), 400
            # Add the current user to the user's friends list
            friend_user['friends'].append(user_email)
            # Remove the friend request from the user's friendRequests.received list
            friend_user['friendRequests']['sent'].remove(user_email)
            user_collection.update_one({"email": friend_email}, {"$set": friend_user})

            # Also remove the friend request from the current user's friendRequests.sent list
            current_user['friendRequests']['received'].remove(friend_email)
            # Add the friend to the current user's friends list
            current_user['friends'].append(friend_email)
            user_collection.update_one({"email": user_email}, {"$set": current_user})

            return jsonify({"message": "Friend request accepted successfully."}), 200
        else:
            # If the user to accept the friend request from is not found, return a 404 error with a message
            return jsonify({"message": "Friend not found."}), 404
    else:
        # If the current user is not found, return a 404 error with a message
        return jsonify({"message": "User not found."}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)  # must be same as gunicorn
