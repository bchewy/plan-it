from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from pymongo import MongoClient, ReturnDocument
from pymongo.errors import ServerSelectionTimeoutError
from config import Config
from datetime import datetime
from functools import wraps
from bson import ObjectId
from flasgger import Flasgger
from flasgger.utils import swag_from
import datetime
import boto3
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "securityDefinitions": {
        "api_key": {
            "type": "apiKey",
            "name": "x-api-key",
            "in": "header"
        }
    },
}


swagger = Flasgger(app, config=swagger_config)
# swagger = Flasgger(app)

app.config.from_object(Config)

client = MongoClient(app.config['MONGO_URI'])
API_KEY = "PlanItIsTheBestProjectEverXYZ"
db = client.wad2
collection = db.routes
user_collection = db.users

@app.after_request
def after_request(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
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


def upload_file_to_s3(file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = 'plan-it/'+file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(
            file_name, 
            'bchewy-images', 
            object_name,
            ExtraArgs={'ACL': 'public-read'}  # Set the ACL to 'public-read'
        )
    except Exception as e:
        print("Error uploading file: ", e)
        return False
    return True

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
# @swag_from('docs/get_api_endpoints.yml')
def get_all_routes():
    """Endpoint returning a list of all available API routes in the application.
    This is using docstrings for specifications.
    ---
    responses:
      200:
        description: A list of all available routes
        schema:
          type: object
          properties:
            routes:
              type: array
              items:
                type: object
                properties:
                  rule:
                    type: string
                  methods:
                    type: array
                    items:
                      type: string
    """
    routes = [{"rule": str(rule), "methods": ', '.join([method for method in rule.methods if method in ['GET', 'POST', 'PUT', 'DELETE']])} for rule in app.url_map.iter_rules()]
    response = jsonify({"routes": routes})
    response.headers['Content-Type'] = 'application/json'
    return response, 200


@app.route("/db")
@require_api_key
def db_check():
    """
    Endpoint to check the health of the database.
    This is using docstrings for specifications.
    ---
    security:
      - api_key: []
    responses:
      200:
        description: Database is healthy.
      500:
        description: Database is unhealthy.
    """
    client = MongoClient('localhost', serverSelectionTimeoutMS=1000)
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        return jsonify({"message": "Database is healthy."}), 200
    except ServerSelectionTimeoutError:
        return jsonify({"message": "Database is unhealthy."}), 500


# Routes ============================================================

# Create (POST)
@app.route("/routes", methods=['POST'])
@require_api_key
def create_route():
    """
    Endpoint to create a new route.
    This endpoint accepts a JSON object containing the route details.
    ---
    tags:
    - Routes
    parameters:
      - name: _id
        in: body
        required: true
        type: string
        example: "653912cb8f5ad5e4f064762e"
      - name: route_id
        in: body
        required: true
        type: string
        example: "route_1698239179224"
      - name: start_point_lat_lng
        in: body
        required: true
        type: string
        example: "Point(1.3690023, 103.8481594)"
      - name: end_point_lat_lng
        in: body
        required: true
        type: string
        example: "Point(1.3341353, 103.8866115)"
      - name: start_point_name
        in: body
        required: true
        type: string
        example: "53 Ang Mo Kio Ave 3, #03-18/19, Singapore 569933"
      - name: end_point_name
        in: body
        required: true
        type: string
        example: "FGA@Playfair 15, Playfair Rd, #03-01, Singapore 367987"
      - name: transport_mode
        in: body
        required: true
        type: string
        example: "DRIVE"
      - name: carbon_emission
        in: body
        required: true
        type: number
        example: 0.94692
      - name: timestamp
        in: body
        required: true
        type: string
        example: "2023-10-25T21:06:19.425+00:00"
      - name: user_id
        in: body
        required: true
        type: string
        example: "brian@bchewy.com"
    security:
      - api_key: []
    responses:
      201:
        description: Route created successfully.
      400:
        description: Bad request.
    """
    data = request.json
    data['timestamp'] = datetime.datetime.now()
    collection.insert_one(data)
    return jsonify({"message": "Route created successfully."}), 201

# Read All (GET)
@app.route("/routes", methods=['GET'])
@require_api_key
def read_all_routes():
    """
    Get all routes
    ---
    tags:
      - Routes
    security:
      - api_key: []
    responses:
      200:
        description: A list of all available routes
        schema:
          type: array
          items:
            type: object
            properties:
              _id:
                type: string
              carbon_emission:
                type: number
              end_point_lat_lng:
                type: string
              end_point_name:
                type: string
              route_id:
                type: string
              start_point_lat_lng:
                type: string
              start_point_name:
                type: string
              timestamp:
                type: string
              transport_mode:
                type: string
              user_id:
                type: string
    """
    all_routes = list(collection.find())
    for route in all_routes:
        route["_id"] = str(route["_id"])
    return jsonify(all_routes), 200

# Read All EMAIL OF USER(GET)
@app.route("/routes/email", methods=['GET'])
@require_api_key
def read_all_routes_email():
    """
    Get all routes for a specific user
    ---
    tags:
      - Routes
    security:
      - api_key: []
    parameters:
      - name: email
        in: query
        type: string
        required: true
        description: The email of the user
    responses:
      200:
        description: A list of all available routes for the user
        schema:
          type: array
          items:
            type: object
            properties:
              _id:
                type: string
              carbon_emission:
                type: number
              end_point_lat_lng:
                type: string
              end_point_name:
                type: string
              route_id:
                type: string
              start_point_lat_lng:
                type: string
              start_point_name:
                type: string
              timestamp:
                type: string
              transport_mode:
                type: string
              user_id:
                type: string
    """
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
    """
    Get a specific route by its route_id
    ---
    tags:
      - Routes
    security:
      - api_key: []
    parameters:
      - name: route_id
        in: path
        type: string
        required: true
        description: The id of the route
    responses:
      200:
        description: The route details
        schema:
          $ref: '#/definitions/Route'
      404:
        description: Route not found
    """

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
    
@app.route("/routes/<route_id>/validate", methods=['PUT'])
@require_api_key
def validate_route(route_id):
    print(route_id)
    updated_route = collection.find_one_and_update(
        {"route_id": route_id}, {"$set": {"validated": True}})
    if updated_route:
        return jsonify({"message": "Route validated successfully."}), 200
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

# =====================================================================================

# User Operations ======================================================================

# Update or create user init into our backend, since we're using auth0
@app.route("/users", methods=['POST', 'PUT'])
@require_api_key
def create_or_update_user():
    """
    Create or update a user
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: auth0_user_id
        in: body
        type: string
        required: true
        description: The auth0 id of the user
      - name: email
        in: body
        type: string
        required: true
        description: The email of the user
      - name: handle
        in: body
        type: string
        required: true
        description: The handle of the user
    responses:
      200:
        description: User updated successfully
        schema:
          $ref: '#/definitions/User'
      201:
        description: User created successfully
        schema:
          $ref: '#/definitions/User'
      400:
        description: auth0_user_id, email, and handle are required
    """
    data = request.json
    # print('User create/update here, data below')
    # print(data)
    # print('\n')
    auth0_user_id = data.get('auth0_user_id')
    email = data.get('email')
    handle = data.get('handle')
    if not auth0_user_id or not email or not handle:
        return jsonify({"message": "auth0_user_id, email, and handle are required."}), 400
    existing_user = user_collection.find_one({"auth0_user_id": auth0_user_id})
    if existing_user:
        updated_user = user_collection.find_one_and_update(
            {"auth0_user_id": auth0_user_id}, {"$set": data}, return_document=ReturnDocument.AFTER)
        if updated_user:
            updated_user["_id"] = str(updated_user["_id"])
            return jsonify({"message": "User updated successfully.", "user": updated_user}), 200
    else:
        data['timestamp'] = datetime.datetime.now()
        data['friends'] = []
        data['friendRequests'] = {"sent": [], "received": []}
        user_collection.insert_one(data)
        return jsonify({"message": "User created successfully."}), 201
    

@app.route("/users/handle/<user_handle>", methods=['GET'])
@require_api_key
def get_user_handle(user_handle):
    """
    Get a specific user by their handle
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: user_handle
        in: path
        type: string
        required: true
        description: The handle of the user
    responses:
      200:
        description: User found successfully
        schema:
          $ref: '#/definitions/User'
      404:
        description: User not found
    """
    user = user_collection.find_one({"handle": user_handle})
    if user:
        user = convert_objectid_to_string(user)
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found."}), 404


@app.route("/users", methods=['GET'])
# @require_api_key
def get_all_users():
    """
    Get all users
    ---
    tags:
      - Users
    security:
      - api_key: []
    responses:
      200:
        description: Users found successfully
        schema:
          $ref: '#/definitions/User'
      404:
        description: No users found
    """
    users = list(user_collection.find({}, {"email": 1, "handle": 1, "level": 1, "pictureurl": 1, "exp": 1, "carbonsavings":1}).sort("level", -1))
    if users:
        users = [convert_objectid_to_string(user) for user in users]
        return jsonify(users), 200
    else:
        return jsonify({"message": "No users found."}), 404

@app.route("/users/<user_email>/carbonsavings", methods=['POST'])
@require_api_key
def add_carbon_savings(user_email):
    """
    Add carbon savings for a user
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            carbonsavings:
              type: number
              description: The carbon savings to add
    responses:
      200:
        description: Carbon savings added successfully
      404:
        description: User not found
    """
    data = request.get_json()
    user = user_collection.find_one({"email": user_email})
    if user:
        user_collection.update_one({"email": user_email}, {"$inc": {"carbonsavings": data['carbonsavings']}})
        return jsonify({"message": "Carbon savings added successfully."}), 200
    else:
        return jsonify({"message": "User not found."}), 404


# Users get individual user ## Internal 
@app.route("/users/iz/<user_email>", methods=['GET'])
@require_api_key
def get_user(user_email):
    """
    Get a specific user by their email
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user
    responses:
      200:
        description: User found successfully
        schema:
          $ref: '#/definitions/User'
      404:
        description: User not found
    """
    user = user_collection.find_one({"email": user_email})
    if user:
        user = convert_objectid_to_string(user)
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found."}), 404

# Users get individual user ## External
@app.route("/users/ez/<user_email>", methods=['GET'])
def ez_get_user(user_email):
    """
    Get a specific user by their email (external)
    ---
    tags:
      - Users
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user
    responses:
      200:
        description: User found successfully
        schema:
          type: object
          properties:
            email:
              type: string
            pictureurl:
              type: string
            exp:
              type: integer
            level:
              type: integer
            friends:
              type: array
              items:
                type: string
      404:
        description: User not found
    """
    user = user_collection.find_one({"email": user_email})
    if user:
        user = convert_objectid_to_string(user)
        user = { "email": user["email"], 
                "pictureurl":user["pictureurl"],
                "exp": user["exp"], 
                "level": user["level"], 
                "friends": user["friends"] }
        return jsonify(user), 201
    else:
        return jsonify({"message": "User not found."}), 200

# Users search for multiple users
@app.route("/users/search/<search_term>", methods=['GET'])
@require_api_key
def search_users(search_term):
    """
    Search for users by a given term
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: search_term
        in: path
        type: string
        required: true
        description: The term to search for users
    responses:
      200:
        description: Users found successfully
        schema:
          type: array
          items:
            type: object
            properties:
              email:
                type: string
              pictureurl:
                type: string
              exp:
                type: integer
              level:
                type: integer
              friends:
                type: array
                items:
                  type: string
      404:
        description: No users found
    """
    if len(search_term) < 5:
        return jsonify({"message": "Please enter at least 5 characters."}), 400
    users = list(user_collection.find({"email": {"$regex": search_term}}))
    if users:
        users = [convert_objectid_to_string(user) for user in users]
        return jsonify(users), 200
    else:
        return jsonify({"message": "No users found."}), 404


# Friend Requests Backend Calls
@app.route("/users/<user_email>/friend_requests", methods=['GET'])
@require_api_key
def get_friend_requests(user_email):
    """
    Get the friend requests of a user
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user
    responses:
      200:
        description: Friend requests retrieved successfully
        schema:
          type: object
          properties:
            sent:
              type: array
              items:
                type: string
            received:
              type: array
              items:
                type: string
      404:
        description: User not found
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
    Send a friend request from the current user to another user
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the current user
      - name: friend_email
        in: body
        type: string
        required: true
        description: The email of the user to send the friend request to
    responses:
      200:
        description: Friend request sent successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Invalid request (e.g., trying to add oneself or friend request already sent)
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    # Find the current user in the database using the provided email
    current_user = user_collection.find_one({"email": user_email})
    friend_email = request.json.get('friend_email')

    if str(user_email) == str(friend_email):
        return jsonify({"message":"you can't add yourself!"}), 400
    if current_user:
        # Get the email of the user to send the friend request to
        # Check if the friend request has already been sent
        if friend_email in current_user['friendRequests']['sent']:
            return jsonify({"message": "Friend request already sent/or already friends!"}), 400
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
    Decline a friend request.
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user who is declining the friend request
      - name: friend_email
        in: body
        schema:
          type: object
          properties:
            friend_email:
              type: string
        required: true
        description: The email of the user who sent the friend request
    responses:
      200:
        description: Friend request declined successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Friend request already declined or not found
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User not found
        schema:
          type: object
          properties:
            message:
              type: string
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
    Accept a friend request from the current user to another user
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user
    responses:
      200:
        description: Friend request accepted successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Friend request already accepted or not found
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User not found
        schema:
          type: object
          properties:
            message:
              type: string
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


# Add levels and exp count to users
@app.route("/users/<user_email>/level", methods=['POST'])
@require_api_key
def add_level(user_email):
    """
    Add level to a user
    ---
    tags:
      - Games
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user
    responses:
      200:
        description: Level added successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Level is required
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        level = request.json.get('level')
        if level:
            # If the user doesn't have a level field, create it and set it to the provided level
            if 'level' not in current_user:
                current_user['level'] = level
            else:
                current_user['level'] += level
            user_collection.update_one({"email": user_email}, {"$set": current_user})
            return jsonify({"message": "Level added successfully."}), 200
        else:
            return jsonify({"message": "Level is required."}), 400
    else:
        return jsonify({"message": "User not found."}), 404
    
@app.route("/users/<user_email>/exp", methods=['POST'])
@require_api_key
def add_exp(user_email):
    """
    Add experience points to the user.
    ---
    tags:
      - Games
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user
      - name: exp
        in: body
        type: integer
        required: true
        description: The amount of experience points to add
    responses:
      200:
        description: EXP added successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: EXP is required
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        exp = request.json.get('exp')
        if exp:
            # If the user doesn't have a level field, create it and set it to the provided level
            if 'exp' not in current_user:
                current_user['exp'] = exp
            else:
                current_user['exp'] += exp

            if current_user['exp'] >= 100:
              current_user['level'] += 1  # Increment level
              current_user['exp'] = 0  # Reset exp
            user_collection.update_one({"email": user_email}, {"$set": current_user})
            return jsonify({"message": "EXP added successfully."}), 200
        else:
            return jsonify({"message": "EXP is required."}), 400
    else:
        return jsonify({"message": "User not found."}), 404

# Replace level
@app.route("/users/<user_email>/replace/level", methods=['POST'])
@require_api_key
def update_level(user_email):
    """
    Update the level of a user
    ---
    tags:
      - Users
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user whose level is being updated
      - name: level
        in: body
        type: integer
        required: true
        description: The new level of the user
    responses:
      200:
        description: Level updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Level is required
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        level = request.json.get('level')
        if level is not None:
            current_user['level'] = level
            user_collection.update_one({"email": user_email}, {"$set": current_user})
            return jsonify({"message": "Level updated successfully."}), 200
        else:
            return jsonify({"message": "Level is required."}), 400
    else:
        return jsonify({"message": "User not found."}), 404

# =====================================================================================



# Post section ======================================================================
@app.route("/users/<user_email>/posts", methods=['POST'])
#@require_api_key
def create_post(user_email):
    """
    Create a post for a user
    ---
    tags:
      - Posts
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user who is creating the post
      - name: content
        in: body
        type: string
        required: true
        description: The content of the post
    responses:
      200:
        description: Post created successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Post content is required
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        post_content = request.json.get('content')
        if post_content:
            badge=request.json.get('badge')
            taggedfriends=request.json.get('taggedfriends')
            post = {"content": post_content,"badge": badge,"taggedfriends":taggedfriends,"timestamp": datetime.datetime.utcnow()}
            current_user['posts'].append(post)
            user_collection.update_one({"email": user_email}, {"$set": current_user})
            return jsonify({"message": "Post created successfully."}), 200
        else:
            return jsonify({"message": "Post content is required."}), 400
    else:
        return jsonify({"message": "User not found."}), 404

@app.route("/users/<user_email>/posts", methods=['GET'])
@require_api_key
def get_posts(user_email):
    """
    Get all posts of a user.
    ---
    tags:
      - Posts
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user whose posts are to be fetched
    responses:
      200:
        description: Posts fetched successfully
        schema:
          type: object
          properties:
            posts:
              type: array
              items:
                type: object
                properties:
                  content:
                    type: string
                  author:
                    type: string
                  timestamp:
                    type: string
      404:
        description: User not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        return jsonify({"posts": current_user['posts']}), 200
    else:
        return jsonify({"message": "User not found."}), 404

# =====================================================================================



# Groups section ======================================================================
@app.route("/users/<user_email>/groups", methods=['POST'])
@require_api_key
def create_group(user_email):
    """
    Create a new group.
    ---
    tags:
      - Groups
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user who is creating the group
      - name: group_name
        in: path
        type: string
        required: true
        description: Group Name
    responses:
      200:
        description: Group created successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Bad request
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    current_user = user_collection.find_one({"email": user_email})
    user_group = db.groups.find_one({"owner_email": user_email})
    group_name = request.json.get('group_name')
    group = db.groups.find_one({"name": group_name})
    
    if not current_user:
        return jsonify({"message": "User not found."}), 404
    if not group_name:
        return jsonify({"message": "Group name is required."}), 400
    if user_group:
        return jsonify({"message": "User has already created a group."}), 400
    if group:
        return jsonify({"message": "Group name already exists."}), 400
    return create_group_success(user_email, group_name)


def create_group_success(user_email, group_name):
    group = {"name": group_name, "owner_email": user_email, "members": [user_email]}
    db.groups.insert_one(group)
    return jsonify({"message": "Group created successfully."}), 200


@app.route("/groups", methods=['GET'])
@require_api_key
def list_all_groups():
    """
    List all groups
    ---
    tags:
      - Groups
    security:
      - api_key: []
    responses:
      200:
        description: List of all groups
        schema:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              owner_email:
                type: string
              members:
                type: array
                items:
                  type: string
      404:
        description: No groups found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    groups = db.groups.find()
    if not groups:
        return jsonify({"message": "No groups found."}), 404
    return jsonify({"groups": [convert_objectid_to_string(group) for group in groups]}), 200



# Join Group
@app.route("/users/<user_email>/groups/<group_name>/join", methods=['POST'])
@require_api_key
def join_group(user_email, group_name):
    """
    Join a group
    ---
    tags:
      - Groups
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user who wants to join the group
      - name: group_name
        in: path
        type: string
        required: true
        description: The name of the group to join
    responses:
      200:
        description: Joined group successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Bad request
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User or Group not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    current_user = user_collection.find_one({"email": user_email})
    group = db.groups.find_one({"name": group_name})
    
    if not current_user:
        return jsonify({"message": "User not found."}), 404
    if not group:
        return jsonify({"message": "Group not found."}), 404
    if user_email in group['members']:
        return jsonify({"message": "Already a member of the group."}), 400
    return join_group_success(user_email, group_name)

def join_group_success(user_email, group_name):
    group = db.groups.find_one({"name": group_name})
    group['members'].append(user_email)
    db.groups.update_one({"name": group_name}, {"$set": group})
    return jsonify({"message": "Joined group successfully."}), 200

# Leave Group
@app.route("/users/<user_email>/groups/<group_name>/leave", methods=['POST'])
@require_api_key
def leave_group(user_email, group_name):
    """
    Leave a group
    ---
    tags:
      - Groups
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user who wants to leave the group
      - name: group_name
        in: path
        type: string
        required: true
        description: The name of the group to leave
    responses:
      200:
        description: Left group successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Bad request
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: User or Group not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        group = db.groups.find_one({"name": group_name})
        if group:
            if user_email in group['members']:
                group['members'].remove(user_email)
                db.groups.update_one({"name": group_name}, {"$set": group})
                return jsonify({"message": "Left group successfully."}), 200
            else:
                return jsonify({"message": "Not a member of the group."}), 400
        else:
            return jsonify({"message": "Group not found."}), 404
    else:
        return jsonify({"message": "User not found."}), 404

# =====================================================================================



# Badges CRUD =========================================================================================================

# Create Badge
@app.route("/badges", methods=['POST'])
@require_api_key
def create_badge():
    """
    ---
    tags:
      - Badges
    security:
      - api_key: []
    parameters:
      - name: name
        in: body
        type: string
        required: true
        description: The name of the badge
      - name: description
        in: body
        type: string
        required: true
        description: The description of the badge
      - name: image
        in: body
        type: string
        required: true
        description: The image of the badge
    responses:
      200:
        description: Badge created successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Name, description and image are required
        schema:
          type: object
          properties:
            message:
              type: string
    """
    data = request.form
    name = data.get('name')
    description = data.get('description')
    image = request.files.get('image')


    # Upload the image to S3 and get the public URL
    image_filename = secure_filename(image.filename)
    image.save(image_filename)
    upload_file_to_s3(image_filename)
    image_url = f"https://bchewy-images.s3.ap-southeast-1.amazonaws.com/plan-it/{image_filename}"
    image = image_url

    if name and description and image:
        badge = {"name": name, "description": description, "image": image}
        db.badges.insert_one(badge)
        return jsonify({"message": "Badge created successfully."}), 200
    else:
        return jsonify({"message": "Name, description and image are required."}), 400


@app.route("/badges", methods=['GET'])
@require_api_key
def get_all_badges():
    """
    Get all badges
    ---
    tags:
      - Badges
    responses:
      200:
        description: Badges retrieved successfully
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: No badges found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    badges = list(db.badges.find())
    for badge in badges:
        badge["_id"] = str(badge["_id"])
    if badges:
        return jsonify(badges), 200
    else:
        return jsonify({"message": "No badges found."}), 404



# Read Badge
@app.route("/badges/<badge_id>", methods=['GET'])
@require_api_key
def read_badge(badge_id):
    """
    Read a badge
    ---
    tags:
      - Badges
    security:
      - api_key: []
    parameters:
      - name: badge_id
        in: path
        type: string
        required: true
        description: The id of the badge
    responses:
      200:
        description: Badge found successfully
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Badge not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    badge = db.badges.find_one({"_id": ObjectId(badge_id)})
    if badge:
        return jsonify(badge), 200
    else:
        return jsonify({"message": "Badge not found."}), 404
    

@app.route("/users/<user_email>/badges", methods=['GET'])
# @require_api_key
def get_user_badges(user_email):
    """
    Get all badges for a user
    ---
    tags:
      - Badges
    security:
      - api_key: []
    parameters:
      - name: user_email
        in: path
        type: string
        required: true
        description: The email of the user
    responses:
      200:
        description: Badges found successfully
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Badges not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    if user_email == "brian@bchewy.com":
        badges = [
        {
            "id": "badge_1",
            "name": "Green Newbie",
            "description": "Congratulations on taking your first step toward a greener planet!",
            "icon": "green_newbie_icon.png",
            "milestone": "First carbon footprint calculation"
            },
            {
            "id": "badge_2",
            "name": "Eco-Friendly Traveler",
            "description": "You've offset the carbon footprint of your travels for one month!",
            "icon": "eco_friendly_traveler_icon.png",
            "milestone": "Offset one month of travel"
            },
            {
            "id": "badge_3",
            "name": "Foodprint Fighter",
            "description": "One week of sustainable eating choices. Way to go!",
            "icon": "foodprint_fighter_icon.png",
            "milestone": "One week of sustainable food choices"
            },
            {
            "id": "badge_4",
            "name": "Solar Superstar",
            "description": "You've converted to using solar energy at home.",
            "icon": "solar_superstar_icon.png",
            "milestone": "Switch to solar energy"
            },
            {
            "id": "badge_5",
            "name": "Recycle Ranger",
            "description": "Recycled items for 30 consecutive days!",
            "icon": "recycle_ranger_icon.png",
            "milestone": "30 days of recycling"
            },
            {
            "id": "badge_6",
            "name": "Community Catalyst",
            "description": "You've inspired 5 friends to join the app and start tracking their footprint.",
            "icon": "community_catalyst_icon.png",
            "milestone": "Refer 5 friends"
            },
            {
            "id": "badge_7",
            "name": "Zero-Waste Warrior",
            "description": "Achieved a zero-waste lifestyle for one month.",
            "icon": "zero_waste_warrior_icon.png",
            "milestone": "One month of zero-waste"
            }
        ]
        
        return jsonify({"badges": badges}), 200
    else:
        return jsonify({"message": "User not found."}), 404


# Update Badge
@app.route("/badges/<badge_id>", methods=['PUT'])
@require_api_key
def update_badge(badge_id):
    """
    Update a badge
    ---
    tags:
      - Badges
    security:
      - api_key: []
    parameters:
      - name: badge_id
        in: path
        type: string
        required: true
        description: The id of the badge
      - name: name
        in: body
        type: string
        required: true
        description: The new name of the badge
      - name: description
        in: body
        type: string
        required: true
        description: The new description of the badge
      - name: image
        in: body
        type: string
        required: true
        description: The new image of the badge
    responses:
      200:
        description: Badge updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
      400:
        description: Name, description and image are required
        schema:
          type: object
          properties:
            message:
              type: string
    """
    name = request.json.get('name')
    description = request.json.get('description')
    image = request.json.get('image')
    if name and description and image:
        badge = {"name": name, "description": description, "image": image}
        db.badges.update_one({"_id": ObjectId(badge_id)}, {"$set": badge})
        return jsonify({"message": "Badge updated successfully."}), 200
    else:
        return jsonify({"message": "Name, description and image are required."}), 400

# Delete Badge
@app.route("/badges/<badge_id>", methods=['DELETE'])
@require_api_key
def delete_badge(badge_id):
    """
    Delete a badge
    ---
    tags:
      - Badges
    security:
      - api_key: []
    parameters:
      - name: badge_id
        in: path
        type: string
        required: true
        description: The id of the badge to delete
    responses:
      200:
        description: Badge deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Badge not found
        schema:
          type: object
          properties:
            message:
              type: string
    """
    db.badges.delete_one({"_id": badge_id})
    return jsonify({"message": "Badge deleted successfully."}), 200

#  =========================================================================================================


# Logging: User Activity Logs =========================================================================================================


@app.route("/users/<user_id>/log", methods=['POST'])
@require_api_key
def log_user_activity(user_id):
    """
    Log user activity
    ---
    tags:
      - Logs
    security:
      - api_key: []
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: The email of the user
      - name: activity
        in: body
        type: string
        required: true
        description: The activity of the user
    responses:
      200:
        description: User activity logged successfully
        schema:
          type: object
          properties:
            message:
              type: string
    """
    activity = request.json.get('activity')
    if activity:
        log = {"user_id": user_id, "activity": activity, "timestamp": datetime.datetime.utcnow()}
        db.user_logs.insert_one(log)
        return jsonify({"message": "User activity logged successfully."}), 200
    else:
        return jsonify({"message": "Activity is required."}), 400


@app.route("/users/<user_id>/logs", methods=['GET'])
@require_api_key
def get_user_logs(user_id):
    """
    Retrieve user logs
    ---
    tags:
      - Logs
    security:
      - api_key: []
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: The id of the user
    responses:
      200:
        description: User logs retrieved successfully
        schema:
          type: array
          items:
            type: object
            properties:
              user_id:
                type: string
              activity:
                type: string
              timestamp:
                type: string
    """
    logs = db.user_logs.find({"user_id": user_id})
    return jsonify({"logs": list(logs)}), 200


# =========================================================================================================


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)  # must be same as gunicorn

