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
    routes = [{"rule": str(rule), "methods": ', '.join([method for method in rule.methods if method in ['GET', 'POST', 'PUT', 'DELETE']])} for rule in app.url_map.iter_rules()]
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
@app.route("/users", methods=['POST', 'PUT'])
@require_api_key
def create_or_update_user():
    """
    This function handles the POST and PUT request at the /users endpoint.
    It either creates a new user or updates an existing user based on the provided auth0_user_id.
    If the auth0_user_id, email, or handle are not provided in the request, it returns a 400 error with a message.
    If the user already exists, it updates the user's data and returns a 200 status code with a success message and the updated user data.
    If the user does not exist, it creates a new user with the provided data, current timestamp, and empty friends and friendRequests lists, and returns a 201 status code with a success message.
    """
    data = request.json
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
        data['timestamp'] = datetime.now()
        data['friends'] = []
        data['friendRequests'] = {"sent": [], "received": []}
        user_collection.insert_one(data)
        return jsonify({"message": "User created successfully."}), 201
    

@app.route("/users/handle/<user_handle>", methods=['GET'])
@require_api_key
def get_user_handle(user_handle):
    """
    This function handles the GET request at the /users/handle/<user_handle> endpoint.
    It retrieves the user with the given handle.
    If the user is found, it returns a JSON object containing the user data.
    If the user is not found, it returns a 404 error with a message.
    """
    user = user_collection.find_one({"handle": user_handle})
    if user:
        user = convert_objectid_to_string(user)
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found."}), 404


# Users get individual user ## Internal 
@app.route("/users/iz/<user_email>", methods=['GET'])
@require_api_key
def get_user(user_email):
    """
    This function handles the GET request at the /users/iz/<user_email> endpoint.
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

# Users get individual user ## External
@app.route("/users/ez/<user_email>", methods=['GET'])
def ez_get_user(user_email):
    """
    This function handles the GET request at the /users/ez/<user_email> endpoint.
    It retrieves the user with the given email.
    If the user is found, it returns a JSON object containing the user's email, exp, and friends level.
    If the user is not found, it returns a 404 error with a message.
    """
    user = user_collection.find_one({"email": user_email})
    if user:
        user = convert_objectid_to_string(user)
        user = { "email": user["email"], 
                "pictureurl":user["pictureurl"],
                "exp": user["exp"], 
                "level": user["level"], 
                "friends": user["friends"] }
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found."}), 404

# Users search for multiple users
@app.route("/users/search/<search_term>", methods=['GET'])
@require_api_key
def search_users(search_term):
    """
    This function handles the GET request at the /users/search/<search_term> endpoint.
    It retrieves the users that match the given search term.
    If any users are found, it returns a JSON array containing the user data.
    If no users are found, it returns a 404 error with a message.
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


# Add levels and exp count to users
@app.route("/users/<user_email>/level", methods=['POST'])
@require_api_key
def add_level(user_email):
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
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        exp = request.json.get('exp')
        if exp:
            # If the user doesn't have a level field, create it and set it to the provided level
            if 'exp' not in current_user:
                current_user['exp'] = exp
            else:
                current_user['exp'] += exp
            user_collection.update_one({"email": user_email}, {"$set": current_user})
            return jsonify({"message": "EXP added successfully."}), 200
        else:
            return jsonify({"message": "EXP is required."}), 400
    else:
        return jsonify({"message": "User not found."}), 404


# Post section
@app.route("/users/<user_email>/posts", methods=['POST'])
@require_api_key
def create_post(user_email):
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        post_content = request.json.get('content')
        if post_content:
            post = {"content": post_content, "author": user_email, "timestamp": datetime.datetime.utcnow()}
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
    current_user = user_collection.find_one({"email": user_email})
    if current_user:
        return jsonify({"posts": current_user['posts']}), 200
    else:
        return jsonify({"message": "User not found."}), 404

# Groups section
@app.route("/users/<user_email>/groups", methods=['POST'])
@require_api_key
def create_group(user_email):
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

# Join Group
@app.route("/users/<user_email>/groups/<group_name>/join", methods=['POST'])
@require_api_key
def join_group(user_email, group_name):
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

# Badges CRUD

# Create Badge
@app.route("/badges", methods=['POST'])
@require_api_key
def create_badge():
    name = request.json.get('name')
    description = request.json.get('description')
    image = request.json.get('image')
    if name and description and image:
        badge = {"name": name, "description": description, "image": image}
        db.badges.insert_one(badge)
        return jsonify({"message": "Badge created successfully."}), 200
    else:
        return jsonify({"message": "Name, description and image are required."}), 400

# Read Badge
@app.route("/badges/<badge_id>", methods=['GET'])
@require_api_key
def read_badge(badge_id):
    badge = db.badges.find_one({"_id": ObjectId(badge_id)})
    if badge:
        return jsonify(badge), 200
    else:
        return jsonify({"message": "Badge not found."}), 404
    

@app.route("/users/<user_email>/badges", methods=['GET'])
# @require_api_key
def get_user_badges(user_email):
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
    db.badges.delete_one({"_id": ObjectId(badge_id)})
    return jsonify({"message": "Badge deleted successfully."}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)  # must be same as gunicorn
