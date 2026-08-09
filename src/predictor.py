import sys
import torch
from typing import Any
from src.logger import logger
from src.exception import CustomException
from config.config import model_config
from src.loader import ModelLoader
from src.utils.text_cleaner import TextCleaner

class SentimentPredictor:
    def __init__(self):
        # The loader handles the Singleton caching logic automatically
        # so this Intializes instantly after first time
        try:
            self.tokenizer, self.model = ModelLoader.load_assets()
        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, raw_text: str) -> dict[str, Any]:
        try:
            if not isinstance(raw_text, str) or not raw_text.strip():
                logger.warning("Empty or invalid input received.")

                return {
                    "label": "Unknown",
                    "confidence": 0.0,
                    "raw_text": raw_text,
                    "cleaned_text": ""
                }

            cleaned_text = TextCleaner.clean(raw_text)

            # Clean the incoming text
            if not cleaned_text:
                logger.warning("Input became empty after preprocessing.")
                return {
                    "label": "Unknown",
                    "confidence": 0.0,
                    "raw_text": raw_text,
                    "cleaned_text": ""
                }
            
            # Tokenize the text using our configured MAX_LEN (64)
            inputs = self.tokenizer(
                cleaned_text,
                return_tensors="pt",
                truncation=True,
                padding="max_length",
                max_length=model_config.MAX_LEN
            ).to(model_config.DEVICE)

            # Model Inference (no_grad disables backprop for speed and memory efficiency)
            with torch.no_grad():
                outputs = self.model(**inputs)
                probabilities = torch.softmax(outputs.logits, dim=-1)[0]

            # Extract and map the highest probability label
            label_idx = torch.argmax(probabilities).item()
            confidence = round(probabilities[label_idx].item() * 100, 2)
            predicted_label = model_config.LABEL_MAPPING.get(label_idx, "Unknown")
            logger.info(
                "Prediction completed successfully. "
                f"Label={predicted_label}, "
                f"Confidence={confidence}%"
            )

            return {
                "label": predicted_label,
                "confidence": confidence,
                "raw_text": raw_text,
                "cleaned_text": cleaned_text,
                "probabilities": {
                    model_config.LABEL_MAPPING[0]: round(probabilities[0].item() * 100, 2),
                    model_config.LABEL_MAPPING[1]: round(probabilities[1].item() * 100, 2),
                }
            }
        except Exception as e:
            logger.exception("Prediction calculation failed.")
            raise CustomException(e, sys)