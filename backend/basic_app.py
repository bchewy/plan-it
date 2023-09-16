from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

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