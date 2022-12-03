from flask import Blueprint, jsonify, request

auth_bp = Blueprint(name="auth", import_name=__name__)

@auth_bp.route('/register', methods=['GET'])
def register():
    """
    ---
    post:
        description: Register a new user to the database.
        responses:
            '201':
                description: User has been created.
                content:
                    application/json:
                        schema: OutputSchema
        tags:
            - 'Authentication functions'
    """
    output = {"msg": "Register OK"}
    return jsonify(output)
