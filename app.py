# Import required libraries
from flask import Flask

# Import all the blueprints/routes
from routes import blueprints

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-very-secure-random-string-here'

# Register all blueprints/route
[app.register_blueprint(bp, url_prefix=prefix) for bp, prefix in blueprints]

# Run the Flask app in debug mode when this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
