import os
import logging
from flask import Blueprint, request, jsonify
from flask import current_app as app


blueprint = Blueprint('main', __name__)

fake_user_db = {
    1: {"name": "Yoru", "email": "yoru@example.com"},
    2: {"name": "Cypher", "email": "cypher@example.com"},
    3: {"name": "Sova", "email": "sova@example.com"},
    }
logger = logging.getLogger(__name__)

# # Home route
# @blueprint.route('/')
# def home():
#     logger.info("Home route accessed")
#     return "Simple API Service"

# Status route to check all routes
@blueprint.route('/health')
def status():
    routes = [
        {'endpoint': '/print', 'method': 'POST', 'data': {'message': 'Hello, World!'}},
        {'endpoint': '/add?num1=1&num2=2', 'method': 'GET'},
        {'endpoint': '/user/1', 'method': 'GET'},
        {'endpoint': '/config', 'method': 'GET'}
    ]
    
    with app.test_client() as client:
        for route in routes:
            if route['method'] == 'POST':
                response = client.post(route['endpoint'], json=route['data'])
            else:
                response = client.get(route['endpoint'])
            if response.status_code != 200:
                logger.error(f"{route['endpoint']} route is not available")
                return 'Service Unavailable', 500
    
    logger.info("All routes are OK")
    return 'OK', 200

# print input route
@blueprint.route('/print', methods=['POST'])
def print_message():
    data = request.get_json()
    message = data.get('message', '')
    
    if not message:
        logger.warning("No message provided in /print route")
        return jsonify({"error": "No message provided"}), 400
    
    logger.info(f"Message received: {message}")
    return jsonify({"print": message})

# Add numbers route
@blueprint.route('/add')
def add_numbers():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    
    if not num1 or not num2:
        logger.warning("Both numbers are required in /add route")
        return jsonify({"error": "Both numbers are required"}), 400
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        logger.error("Non-numeric input provided in /add route")
        return jsonify({"error": "Both numbers must be numeric"}), 400

    result = num1 + num2
    logger.info(f"Addition result: {result}")
    return jsonify({"result": result})

# Get user route
@blueprint.route('/user/<int:user_id>')
def get_user(user_id):
    user = fake_user_db.get(user_id)
    if user:
        logger.info(f"User found: {user.get('name')}")
        return jsonify(user)
    else:
        logger.warning(f"User not found: {user_id}")
        return jsonify({"error": "User not found"}), 404

# GET config values
@blueprint.route('/config')
def get_config():
    config = {
        "LOGGING_LEVEL": app.config['LOGGING_LEVEL'],
        "COUNT_VALUE": app.config['COUNT_VALUE'],
        "USER_NAME": app.config['USER_NAME']
    }
    return jsonify(config)
