import sys
from flask import jsonify, render_template, Blueprint, request
from src.predictor import SentimentPredictor
from src.logger import logger

# Blueprint for the routes
main_blueprint = Blueprint('main', __name__)

# Initialize the predictor -- The Singleton loader ensures this is highly efficient
try:
    logger.info("Initializing Sentiment Predictor in Flask Routes")
    predictor = SentimentPredictor()
except Exception as e:
    logger.critical("Failed to Initialize Sentiment Predictor. Shutting Down")
    sys.exit(1)

# Serves the main frontend UI.
@main_blueprint.route('/')
def home():
    return render_template('index.html')

# Handles incoming prediction requests from the frontend.
@main_blueprint.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Validate that the request contains text
        if not data or 'text' not in data:
            logger.warning("Predict Endpoint hit with Missing data")
            return jsonify({'error': "No text Provided"}), 400
        raw_text = data['text']

        # Run the Prediction through the Model
        prediction_result = predictor.predict(raw_text)
        return jsonify(prediction_result), 200
    except Exception as e:
        logger.exception("Error occurred during the prediction")
        return jsonify({'error': "An internal server error Occurred"}), 500