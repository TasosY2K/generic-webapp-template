# load libaries
from flask import Flask, jsonify
import sys
from src.api_spec import spec

# load modules
from src.blueprints.auth import auth_bp
from src.blueprints.swagger import swagger_ui_blueprint, SWAGGER_URL

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

with app.test_request_context():
    # register all swagger documented functions here
    for fn_name in app.view_functions:
        if fn_name == 'static':
            continue
        print(f"Loading swagger docs for function: {fn_name}")
        view_fn = app.view_functions[fn_name]
        spec.path(view=view_fn)

@app.route("/api/swagger.json")
def create_swagger_spec():
    return jsonify(spec.to_dict())