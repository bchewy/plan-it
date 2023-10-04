from flask import Flask, request, jsonify
from flask_cors import CORS
from flash_pymongo import PyMongo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

CORS(app)


@app.route("/health")
def health_check():
	return jsonify(
        	{
            	"message": "Service is healthy."
        	}
	), 200


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)