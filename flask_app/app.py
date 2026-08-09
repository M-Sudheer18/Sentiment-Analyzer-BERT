import sys 
from flask import Flask
from src.logger import logger
from config.config import app_config
from flask_app.routes import main_blueprint

# Initialize the Flask application
def create_app():
    app = Flask(__name__)
    # Register the routes blueprint
    app.register_blueprint(main_blueprint)
    return app

if __name__ == '__main__':
    try:
        app = create_app()
        logger.info(
            f"Starting Flask server on Post {app_config.FLASK_PORT} | "
            f"Debug Mode {app_config.DEBUG}"
        )

        # python -m flask_app.app
        print(f"Running on http://localhost:{app_config.FLASK_PORT}")
        app.run(
            host="0.0.0.0",
            port=app_config.FLASK_PORT,
            debug=app_config.DEBUG
        )
    except Exception as e:
        logger.info("Failed to Start Flask Application")
        sys.exit(1)