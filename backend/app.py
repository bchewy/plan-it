from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient, ReturnDocument
from pymongo.errors import ServerSelectionTimeoutError
from config import Config
from datetime import datetime
from functools import wraps
from bson import ObjectId

API_KEY = "PlanItIsTheBestProjectEverXYZ"

app = Flask(__name__)
app.config.from_object(Config)
client = MongoClient(app.config['MONGO_URI'])

CORS(app)

# Database init
db = client.wad2
collection = db.routes
user_collection = db.users
friends_collection = db.friends
friend_requests_collection = db.friend_requests


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

# @require_api_key
# def health_check():
#     return jsonify(
#         {
#             "message": "Service is healthy."
#         }
#     ), 200


# Database healthcheck


@app.route("/db")
# @require_api_key
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


###########################################################################################################################################################################
###################################################################################################
############################################################################################################
########################################################################
################################################################################################################################################################
###################################################################################################
############################################################################################################
########################################################################################################################################################################################################################################
###################################################################################################
############################################################################################################
########################################################################


# This is an internal API call, only meant for the frontend to call our backend database to sync with auth0 users.
# @app.route("/users", methods=['POST'])
# @require_api_key
# def create_or_update_user():
#     data = request.json
#     print(data)
#     auth0_user_id = data.get('auth0_user_id')
#     email = data.get('email')
#     # Validate the data
#     if not auth0_user_id or not email:
#         return jsonify({"message": "Both auth0_user_id and email are required."}), 400
#     # Check if user exists
#     existing_user = user_collection.find_one({"auth0_user_id": auth0_user_id})
#     if existing_user:
#         # Update user data if necessary
#         updated_user = user_collection.find_one_and_update(
#             {"auth0_user_id": auth0_user_id}, {"$set": data}, return_document=ReturnDocument.AFTER)
#         if updated_user:
#             updated_user["_id"] = str(updated_user["_id"])
#             return jsonify({"message": "User updated successfully.", "user": updated_user}), 200
#     else:
#         # Create new user document
#         data['timestamp'] = datetime.now()
#         user_collection.insert_one(data)
#         return jsonify({"message": "User created successfully."}), 201


# @app.route("/users/search", methods=['GET'])
# @require_api_key
# def search_users():
#     # This is an internal API call, only meant for the frontend to call our backend database to sync with auth0 users.
#     # Validate the data
#     email = request.args.get('email')
#     if not email:
#         return jsonify({"message": "Email is required."}), 400
#     users = list(user_collection.find({"email": email}))
#     if not users:
#         return jsonify({"message": "User not found."}), 404
#     for user in users:
#         user["_id"] = str(user["_id"])
#     return jsonify(users), 200


# @app.route("/friends", methods=['POST'])
# @require_api_key
# def add_friend():
#     data = request.json
#     user_id = data.get('user_id')
#     user_email = data.get('user_email')
#     friend_email = data.get('friend_email')

#     # Check if the user is trying to add themselves
#     if user_email == friend_email:
#         return jsonify({"message": "You can't add yourself!"}), 400

#     # Check if friend exists in the users database
#     friend = user_collection.find_one({"email": friend_email})
#     if not friend:
#         return jsonify({"message": "Friend not found in users database."}), 404

#     # Check if friend is already added
#     user = friends_collection.find_one({"user_id": user_id})
#     if user and friend_email in user.get('friends', []):
#         return jsonify({"message": "Friend already added."}), 400

#     # Add friend to the user's document
#     friends_collection.update_one(
#         {"user_id": user_id},
#         {"$set": {"user_email": user_email}, "$push": {"friends": friend_email}},
#         upsert=True
#     )
#     return jsonify({"message": "Friend added successfully."}), 201


# @app.route("/friends", methods=['GET'])
# @require_api_key
# def list_friends():
#     email = request.args.get('email')
#     user = friends_collection.find_one({"user_email": email})
#     if user:
#         friends = user.get('friends', [])
#     else:
#         friends = []
#     return jsonify(friends), 200


# @app.route("/friend_requests", methods=['POST'])
# @require_api_key
# def create_friend_request():
#     data = request.json
#     sender_email = data.get('sender_email')
#     receiver_email = data.get('receiver_email')

#     # Check if body contains the two fields
#     if not sender_email or not receiver_email:
#         return jsonify({"message": "Both sender and receiver emails are required."}), 400

#     # Check if the user is trying to add themselves
#     if sender_email == receiver_email:
#         return jsonify({"message": "You can't send a friend request to yourself!"}), 400

#     # Check if receiver exists in the users database
#     receiver = user_collection.find_one({"email": receiver_email})
#     if not receiver:
#         return jsonify({"message": "This user was not found."}), 404

#     friend_requests_collection.insert_one(
#         {"sender_email": sender_email, "receiver_email": receiver_email}
#     )
#     return jsonify({"message": "Friend request sent."}), 201


# # Fetch all friend requests for this user based on their email
# @app.route("/friend_requests", methods=['GET'])
# @require_api_key
# def list_friend_requests():
#     print('Looking for friend requests')
#     email = request.args.get('email')
#     if not email:
#         return jsonify({"message": "Email is required."}), 400
#     friend_request = friend_requests_collection.find_one(
#         {"receiver_email": email})
#     print(friend_request)
#     if friend_request:
#         sent_requests = friend_request.get('sent_requests', [])
#     else:
#         sent_requests = []
#     return jsonify(sent_requests), 200


# @app.route("/friend_requests/<request_id>", methods=['PUT'])
# @require_api_key
# def accept_friend_request(request_id):
#     # Move the friend request from the friend_requests collection to the friends collection
#     friend_request = friend_requests_collection.find_one_and_delete(
#         {"_id": ObjectId(request_id)})
#     if friend_request:
#         friends_collection.update_one(
#             {"user_email": friend_request['sender_email']},
#             {"$push": {"friends": friend_request['receiver_email']}},
#             upsert=True
#         )
#         return jsonify({"message": "Friend request accepted."}), 200
#     else:
#         return jsonify({"message": "Friend request not found."}), 404


# @app.route("/friend_requests/<request_id>", methods=['DELETE'])
# @require_api_key
# def decline_friend_request(request_id):
#     # Remove the friend request from the friend_requests collection
#     result = friend_requests_collection.delete_one(
#         {"_id": ObjectId(request_id)})
#     if result.deleted_count > 0:
#         return jsonify({"message": "Friend request declined."}), 200
#     else:
#         return jsonify({"message": "Friend request not found."}), 404


###########################################################################################################################################################################
###################################################################################################
############################################################################################################
########################################################################
################################################################################################################################################################
###################################################################################################
############################################################################################################
########################################################################################################################################################################################################################################
###################################################################################################
############################################################################################################
########################################################################


@app.route("/users", methods=['POST'])
def create_or_update_user():
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
        # Get friendRequests or initialize as empty dictionary if it doesn't exist
        friend_requests = user.get('friendRequests', {})
        # Ensure 'sent' and 'received' keys exist in the dictionary
        friend_requests.setdefault('sent', [])
        friend_requests.setdefault('received', [])
        # Convert ObjectId to string
        friend_requests['sent'] = [str(request_id)
                                   for request_id in friend_requests['sent']]
        friend_requests['received'] = [
            str(request_id) for request_id in friend_requests['received']]
        return jsonify(friend_requests), 200
    else:
        # If the user is not found, return a 404 error with a message
        return jsonify({"message": "User not_found."}), 404


@app.route("/friend_requests", methods=['POST'])
def create_friend_request():
    data = request.json
    sender_email = data.get('sender_email')
    receiver_email = data.get('receiver_email')
    if not sender_email or not receiver_email:
        return jsonify({"message": "Both sender and receiver emails are required."}), 400
    if sender_email == receiver_email:
        return jsonify({"message": "You can't send a friend request to yourself!"}), 400
    receiver = user_collection.find_one({"email": receiver_email})
    if not receiver:
        return jsonify({"message": "This user was not found."}), 404
    sender = user_collection.find_one({"email": sender_email})
    if not sender:
        return jsonify({"message": "Sender not found."}), 404
    friend_request = {"sender_email": sender_email,
                      "receiver_email": receiver_email}
    friend_requests_collection.insert_one(friend_request)
    user_collection.update_one({"email": sender_email}, {
                               "$push": {"friendRequests.sent": friend_request["_id"]}})
    user_collection.update_one({"email": receiver_email}, {
                               "$push": {"friendRequests.received": friend_request["_id"]}})
    return jsonify({"message": "Friend request sent."}), 201


@app.route("/friend_requests/<request_id>", methods=['PUT'])
def accept_friend_request(request_id):
    friend_request = friend_requests_collection.find_one_and_delete(
        {"_id": ObjectId(request_id)})
    if friend_request:
        sender = user_collection.find_one(
            {"email": friend_request['sender_email']})
        receiver = user_collection.find_one(
            {"email": friend_request['receiver_email']})
        if sender and receiver:
            user_collection.update_one({"_id": sender["_id"]}, {"$pull": {
                                       "friendRequests.sent": friend_request["_id"]}, "$push": {"friends": receiver["_id"]}})
            user_collection.update_one({"_id": receiver["_id"]}, {"$pull": {
                                       "friendRequests.received": friend_request["_id"]}, "$push": {"friends": sender["_id"]}})
            return jsonify({"message": "Friend request accepted."}), 200
    return jsonify({"message": "Friend request not found."}), 404


@app.route("/friend_requests/<request_id>", methods=['DELETE'])
def decline_friend_request(request_id):
    friend_request = friend_requests_collection.find_one_and_delete(
        {"_id": ObjectId(request_id)})
    if friend_request:
        sender = user_collection.find_one(
            {"email": friend_request['sender_email']})
        receiver = user_collection.find_one(
            {"email": friend_request['receiver_email']})
        if sender and receiver:
            user_collection.update_one({"_id": sender["_id"]}, {
                                       "$pull": {"friendRequests.sent": friend_request["_id"]}})
            user_collection.update_one({"_id": receiver["_id"]}, {
                                       "$pull": {"friendRequests.received": friend_request["_id"]}})
            return jsonify({"message": "Friend request declined."}), 200
    return jsonify({"message": "Friend request not found."}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)  # must be same as gunicorn
