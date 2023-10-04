from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
client = MongoClient("localhost", 27017)
# mongo = PyMongo(app)

CORS(app)


@app.route("/")
def health_check():
	return jsonify(
        	{
            	"message": "Service is healthy."
        	}
	), 200


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888, debug=True) # must be same as gunicorn