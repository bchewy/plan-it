from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/modules'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)


class Module(db.Model):
    __tablename__ = 'module'

    module_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    section = db.Column(db.String(10), nullable=False)

    def __init__(self, name, section):
        self.name = name
        self.section = section

    def to_dict(self):
        return {
            "module_id": self.module_id,
            "name": self.name,
            "section": self.section
        }


@app.route("/modules/health")
def health_check():
	return jsonify(
        	{
            	"message": "Service is healthy."
        	}
	), 200


@app.route("/modules")
def get_all():
    modules = Module.query.all()
    if len(modules) != 0:
        return jsonify(
            {
                "data": {
                    "modules": [module.to_dict() for module in modules]
                }
            }
        ), 200
    return jsonify(
        {
            "message": "No modules in database."
        }
    ), 200


@app.route("/modules/<int:module_id>")
def find_module_by_id(module_id):
    module = Module.query.filter_by(module_id=module_id).first()
    if module:
        return jsonify(
            {
                "data": module.to_dict()
            }
        ), 200
    return jsonify(
        {
            "message": "Module with ID " + str(module_id) + " not found."
        }
    ), 404


@app.route("/modules", methods=['POST'])
def new_module():
    try:
        data = request.get_json()
        module = Module(**data)
        db.session.add(module)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "message": "Error creating module.",
                "error": str(e)
            }
        ), 500

    return jsonify(
        {
            "message": "Module created successfully.",
            "data": module.to_dict()
        }
    ), 201


@app.route("/modules/<int:module_id>", methods=['PUT'])
def replace_module(module_id):
    module = Module.query.filter_by(module_id=module_id).first()
    if module is None:
        return jsonify(
            {
                "message": "Module with ID " + str(module_id) + " not found."
            }
        ), 404
    data = request.get_json()
    if all(key in data.keys() for key in ('name', 'section')):
        module.name = data['name']
        module.section = data['section']
        try:
            db.session.commit()
        except Exception as e:
            return jsonify(
                {
                    "message": "Error replacing module.",
                    "error": str(e)
                }
            ), 500
        return jsonify(
            {
                "message": "Module replaced successfully.",
                "data": module.to_dict()
            }
        ), 200
    return jsonify(
        {
            "message": "An error occurred replacing the game.",
            "error": "Keys are missing from the JSON object. " +
                     " Consider HTTP PATCH instead."
        }
    ), 500


@app.route("/modules/<int:module_id>", methods=['PATCH'])
def update_module(module_id):
    module = Module.query.with_for_update(of=Module)\
               .filter_by(module_id=module_id).first()
    if module is None:
        return jsonify(
            {
                "message": "Module with ID " + str(module_id) + " not found."
            }
        ), 404
    data = request.get_json()
    if 'name' in data.keys():
        module.name = data['name']
    if 'section' in data.keys():
        module.section = data['section']

    try:
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "message": "Error updating module.",
                "error": str(e)
            }
        ), 500
    return jsonify(
        {
            "message": "Module updated successfully.",
            "data": module.to_dict()
        }, 200
    )


@app.route("/modules/<int:module_id>", methods=['DELETE'])
def delete_module(module_id):
    module = Module.query.filter_by(module_id=module_id).first()
    if module is not None:
        try:
            db.session.delete(module)
            db.session.commit()
        except Exception as e:
            return jsonify(
                {
                    "message": "Error deleting module.",
                    "error": str(e)
                }
            ), 500
        return jsonify(
            {
                "message": "Module deleted successfully.",
                "data": {
                    "module_id": module_id
                }
            }
        ), 200
    return jsonify(
        {
            "message": "Module with ID " + str(module_id) + " not found."
        }
    ), 404


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)


#1234test
    #test123
