import os
import sys
import nltk
import streamlit as st
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="flask_app/static/images/favicon.ico",
    layout="centered",
    initial_sidebar_state="expanded"
)

from src.logger import logger
from src.predictor import SentimentPredictor
from st_app.components.sidebar import render_sidebar

# Cache the predictor so it only loads once into memory!
@st.cache_resource
def load_model():
    try:
        logger.info("Initializing Sentiment Predictor...")
        return SentimentPredictor()
    except Exception as e:
        logger.critical(f"Failed to Initialize Sentiment Predictor: {e}")
        st.error("Critical Error: Failed to load the model. Check terminal logs.")
        st.stop()

def main():
    # Bert Model
    predictor = load_model()

    # Sidebar
    render_sidebar()

    # Header
    st.title("Sentiment Intelligence")
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": "Welcome, Sudheer. The BERT Sentiment model is loaded and ready. Enter your text below to analyze its sentiment."
            }
        ]
    # Render existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input Box
    if prompt := st.chat_input("Type your text here to analyze sentiment..."):
        # Display user message immediately
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Process Prediction with a loading spinner
        with st.chat_message("assistant"):
            with st.spinner("Analyzing Input"):
                try:
                    # Call Model
                    result = predictor.predict(prompt)
                    label = result["label"]
                    confidence = result["confidence"]

                    # Format the output
                    color = "green" if label == "Positive" else "red"
                    response_text = (
                        f"**Prediction**\n\n"
                        f"Sentiment: :{color}[**{label}**]\n\n"
                        f"Confidence: {confidence}%\n\n"
                        f"*Processed by BERT*"
                    )
                    st.markdown(response_text)

                    # Save to states
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                    st.session_state.history.append({"text": prompt, "label": label})
                except Exception as e:
                    logger.exception("Streamlit Prediction Error")
                    st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
