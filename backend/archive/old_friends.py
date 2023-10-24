@app.route("/friend_requests", methods=['POST'])
@require_api_key
def send_friend_request():
    data = request.json
    sender_id = data.get('sender_id')
    sender_email = data.get('sender_email')
    receiver_email = data.get('receiver_email')

    # Check if the user is trying to send a request to themselves
    if sender_email == receiver_email:
        return jsonify({"message": "You can't send a friend request to yourself!"}), 400

    # Check if receiver exists in the users database
    receiver = user_collection.find_one({"email": receiver_email})
    if not receiver:
        return jsonify({"message": "Receiver not found in users database."}), 404

    # Check if friend request is already sent
    sender = friend_requests_collection.find_one({"sender_id": sender_id})
    if sender and receiver_email in sender.get('sent_requests', []):
        return jsonify({"message": "Friend request already sent."}), 400

    # Send friend request
    friend_requests_collection.update_one(
        {"sender_id": sender_id},
        {"$set": {"sender_email": sender_email},
            "$push": {"sent_requests": receiver_email}},
        upsert=True
    )
    return jsonify({"message": "Friend request sent successfully."}), 201


@app.route("/friend_requests", methods=['GET'])
@require_api_key
def list_friend_requests():
    email = request.args.get('email')
    user = friend_requests_collection.find_one({"sender_email": email})
    if user:
        sent_requests = user.get('sent_requests', [])
    else:
        sent_requests = []
    return jsonify(sent_requests), 200
