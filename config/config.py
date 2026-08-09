import os
from pathlib import Path
from dataclasses import dataclass, field
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
# Load environment variables from .env file if it exists
load_dotenv(os.path.join(BASE_DIR, ".env"))

@dataclass(frozen=True)
class ModelConfig:
    # Hugging Face Repository
    HF_MODEL_REPO: str = os.getenv("HF_MODEL_REPO", "Sudheer17/Sentiment")
    HF_SUBFOLDER: str = "BERT"

    # Model inference
    MAX_LEN: int = 64
    BATCH_SIZE: int = 32
    DEVICE: str = "cuda" if os.getenv("USE_CUDA") == "True" else "cpu"
    LABEL_MAPPING: dict = field(init=False)


    # Sentiment140 labels: 0 mapped to Negative, 1 mapped to Positive
    def __post_init__(self):
        object.__setattr__(
            self,
            "LABEL_MAPPING",
            {
                0: "Negative",
                1: "Positive"
            }
        )

@dataclass(frozen=True)
class AppConfig:
    # web Application
    FLASK_PORT  : int = int(os.getenv("FLASK_PORT", 5000))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

# Instantiate the configurations so they can be imported cleanly across the app
model_config = ModelConfig()
app_config = AppConfig()