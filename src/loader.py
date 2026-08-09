import sys
from src.logger import logger
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from config.config import model_config
from src.exception import CustomException

class ModelLoader:
    _model = None
    _tokenizer = None

    @classmethod
    def load_assets(cls):
        # Loads the tokenizer and model into memory once.
        if cls._model is None or cls._tokenizer is None:
            try:
                logger.info(
                    f"Loading model from Hugging Face repository: "
                    f"{model_config.HF_MODEL_REPO}/{model_config.HF_SUBFOLDER}"
                )

                # Load Tokenizer 
                logger.info("Downloading/Loading Tokenizer...")
                cls._tokenizer = AutoTokenizer.from_pretrained(
                    model_config.HF_MODEL_REPO,
                    subfolder=model_config.HF_SUBFOLDER
                )
                # Load BERT Model
                logger.info("Downloading/Loading BERT Model...")
                cls._model = AutoModelForSequenceClassification.from_pretrained(
                    model_config.HF_MODEL_REPO,
                    subfolder=model_config.HF_SUBFOLDER
                )

                # Move to configured device (CPU/GPU) and set to evaluation mode
                logger.info(
                    f"Moving model to "
                    f"{model_config.DEVICE.upper()} "
                    f"and setting evaluation mode."
                )
                cls._model.to(model_config.DEVICE)
                cls._model.eval()
                logger.info("Model and Tokenizer successfully loaded into memory.")

            except Exception as e:
                logger.exception("Failed to load model/tokenizer.")
                raise CustomException(e, sys)
        else:
            logger.info("Model and Tokenizer are already loaded. Serving from cache.")

        return cls._tokenizer, cls._model