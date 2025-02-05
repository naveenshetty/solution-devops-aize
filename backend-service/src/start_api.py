from flask_cors import CORS
from api import create_app
app = create_app()
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
