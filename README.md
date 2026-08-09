<div align="center">

<h1>🎭 Sentiment Intelligence — BERT</h1>

## **THINK BIG. BUILD SMART.**

**A Deep-Learning-Powered Sentiment Analysis Platform**

Fine-tuned **BERT** model for real-time sentiment classification with confidence scoring, modern web interfaces, and production-ready deployment.

**Positive · Negative · BERT · PyTorch · Hugging Face**

</div>

---

## 🚀 Project Overview

**Sentiment Intelligence — BERT** is an end-to-end NLP sentiment analysis platform powered by a fine-tuned **BERT Transformer model**.

The system accepts natural-language text and instantly predicts its sentiment as:

* 🟢 **Positive**
* 🔴 **Negative**

Along with the predicted sentiment, the application provides a **confidence percentage** representing the model's prediction probability.

The project includes **two complete interfaces**:

* 🌐 **Flask REST API + JavaScript Frontend**
* 📊 **Streamlit Interactive Dashboard**

The trained BERT model is hosted on **Hugging Face Hub** and can be dynamically downloaded during inference.

---

## 🔗 Live Links & Resources

| Resource                  | Link                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------- |
| 🚀 **Live Streamlit App** | [Launch Deployed Application](YOUR_STREAMLIT_DEPLOYMENT_LINK)                         |
| 🤗 **Hugging Face Model** | [Sudheer17/Sentiment](https://huggingface.co/Sudheer17/Sentiment)                     |
| 💻 **GitHub Repository**  | [Sentiment-Analyzer---BERT](https://github.com/M-Sudheer18/Sentiment-Analyzer---BERT) |
| 👔 **LinkedIn Profile**   | [Connect on LinkedIn](https://www.linkedin.com/in/sudheer-muthyala-317180268)         |

---

## ✨ Key Features

### 🤖 BERT-Powered Inference

Fine-tuned **BERT Transformer architecture** provides contextual understanding for sentiment classification.

### 🌐 Dual Interface Deployment

The project provides both:

* **Flask REST API + JavaScript frontend**
* **Streamlit dashboard**

### ☁️ Dynamic Model Loading

The trained model is remotely loaded directly from **Hugging Face Hub**, eliminating the need to store model weights inside the application repository.

### 🎯 Confidence Scoring

Every prediction includes a probability-based confidence score.

**Example:**

```text
Sentiment: Positive
Confidence: 96.84%
```

### 🧹 Robust Text Preprocessing

A custom **NLTK preprocessing pipeline** performs text cleaning, tokenization, stop-word filtering, and lemmatization before inference.

### 🌑 Modern Dark UI

A minimalist SaaS-inspired interface designed for a clean and interactive sentiment-analysis experience.

### 📜 Execution History

The application maintains prediction history to make previous sentiment-analysis results easy to track.

---

## 🧠 How the System Works

```text
                    ┌─────────────────────┐
                    │    User Text Input  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Text Preprocessing │
                    │        NLTK         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    BERT Tokenizer   │
                    │   PyTorch Tensors   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Fine-Tuned BERT    │
                    │       Model         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Softmax       │
                    │ Probability Scores  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Sentiment +         │
                    │ Confidence Score    │
                    └─────────────────────┘
```

---

## 📊 Example Prediction

### Input

```text
The movie was absolutely brilliant! Highly recommended.
```

### Output

```text
Prediction
────────────────────────────
Sentiment    : Positive
Confidence   : 96.84%
Model        : BERT
Status       : Processed Successfully
```

---

## 🛠️ Technology Stack

| Category                     | Technology                   |
| ---------------------------- | ---------------------------- |
| 🐍 **Core Language**         | Python 3.13.5                |
| 🧠 **Deep Learning**         | PyTorch                      |
| 🤗 **Transformer Framework** | Hugging Face Transformers    |
| 🔤 **NLP**                   | NLTK                         |
| 🌐 **Backend API**           | Flask                        |
| 📊 **Dashboard**             | Streamlit                    |
| 🎨 **Frontend**              | HTML5, CSS3, JavaScript ES6+ |
| 📦 **Model Hosting**         | Hugging Face Hub             |
| 🔧 **Version Control**       | Git & GitHub                 |

---

## 📂 Project Structure

```text
Sentiment-Analyzer---BERT/
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── docs/
│
├── flask_app/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── __init__.py
│   ├── app.py
│   └── routes.py
│
├── Notebooks/
│
├── src/
│   ├── utils/
│   │   ├── __init__.py
│   │   └── text_cleaner.py
│   │
│   ├── __init__.py
│   ├── exception.py
│   ├── loader.py
│   ├── logger.py
│   └── predictor.py
│
├── st_app/
│   ├── .streamlit/
│   ├── components/
│   └── app.py
│
├── .gitignore
├── .python-version
├── MODEL.md
├── README.md
├── requirements.txt
└── runtime.txt
```

---

# 🌐 Quickstart — Deployed Application

Open the **Live Streamlit Application** in your browser.

Enter any sentence, review, comment, or natural-language text into the chat input.

### Example

```text
The movie was absolutely brilliant! Highly recommended.
```

Press **Enter** to submit the text.

The application processes the input through the BERT inference pipeline and returns:

```text
┌──────────────────────────────────────┐
│              PREDICTION              │
├──────────────────────────────────────┤
│ Sentiment  : Positive                │
│ Confidence : 96.84%                  │
│ Model      : BERT                    │
└──────────────────────────────────────┘
```

---

# 💻 Local Setup & Installation

Follow the steps below to run the project locally.

## Prerequisites

Make sure the following are installed:

* Python **3.13.5**
* Git

---

## 1️⃣ Clone the Repository

Open your terminal or command prompt:

```bash
git clone https://github.com/M-Sudheer18/Sentiment-Analyzer---BERT.git
cd Sentiment-Analyzer---BERT
```

---

## 2️⃣ Verify Python Version

```bash
python --version
```

Expected output:

```text
Python 3.13.5
```

---

## 3️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Download NLTK Resources

Run the following command to download the required NLTK language resources:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('omw-1.4')"
```

The project uses these resources for its text preprocessing pipeline.

---

# 🌐 6️⃣ Run the Flask Application

Start the Flask application from the project root:

```bash
python -m flask_app.app
```

Then open:

```text
http://localhost:5000
```

Use the web interface to enter text and test the live prediction routes.

---

# 📊 7️⃣ Run the Streamlit Application

Open a new terminal with the virtual environment activated and execute:

```bash
streamlit run st_app/app.py
```

The Streamlit dashboard will be available at:

```text
http://localhost:8501
```

---

# ⚙️ Inference Pipeline

The complete prediction workflow follows this sequence:

```text
User Input
    │
    ▼
┌──────────────────────────────┐
│ Text Cleaning                │
│ • Tokenization               │
│ • Stop-word filtering        │
│ • Lemmatization              │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ BERT Tokenizer               │
│ • Token IDs                  │
│ • Attention Masks            │
│ • PyTorch Tensors            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Fine-Tuned BERT Model        │
│ Hosted on Hugging Face Hub   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Softmax                      │
│ Probability Distribution     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Final Prediction             │
│                              │
│ Positive / Negative          │
│ +                            │
│ Confidence Percentage        │
└──────────────────────────────┘
```

---

# 🔬 NLP Preprocessing

Before the text reaches the BERT model, the application applies a custom **NLTK-based preprocessing pipeline**.

### Processing stages

```text
Raw Text
   │
   ├── Tokenization
   │
   ├── Stop-word Filtering
   │
   ├── Lemmatization
   │
   └── Cleaned Text
          │
          ▼
     BERT Tokenizer
```

This preprocessing layer helps normalize the incoming text before transformer-based inference.

---

# 🤗 Model Hosting

The fine-tuned sentiment model is hosted on **Hugging Face Hub**.

### Model

**Sudheer17/Sentiment**

The application dynamically downloads and loads the model when required, allowing the trained model to remain separate from the application source code.

Model resource:

**https://huggingface.co/Sudheer17/Sentiment**

---

# 🧩 Application Architecture

```text
                    SENTIMENT INTELLIGENCE
                            │
             ┌──────────────┴──────────────┐
             │                             │
             ▼                             ▼
       Flask Application             Streamlit App
             │                             │
             ▼                             ▼
      JS + HTML + CSS              Interactive UI
             │                             │
             └──────────────┬──────────────┘
                            │
                            ▼
                    Prediction Engine
                            │
                            ▼
                    Text Preprocessor
                            │
                            ▼
                     BERT Tokenizer
                            │
                            ▼
                  Fine-Tuned BERT Model
                            │
                            ▼
                      Probability
                            │
                            ▼
                Sentiment + Confidence
```

---

# 📁 Core Components

### `config/`

Centralized configuration and project settings.

### `flask_app/`

Contains the Flask backend, REST routes, templates, JavaScript, CSS, and frontend assets.

### `src/`

Core machine-learning and application utilities.

Important components include:

* `loader.py` — Model loading
* `predictor.py` — Sentiment prediction
* `logger.py` — Logging functionality
* `exception.py` — Exception handling
* `text_cleaner.py` — NLP preprocessing

### `st_app/`

Contains the Streamlit application and its supporting components.

### `Notebooks/`

Development and experimentation notebooks used throughout the model-building workflow.

### `MODEL.md`

Model-specific documentation.

### `requirements.txt`

Python dependencies required to run the project.

---

# 🎯 Supported Sentiments

The current BERT sentiment classifier provides two classification outcomes:

| Label           | Meaning                                  |
| --------------- | ---------------------------------------- |
| 🟢 **Positive** | The text expresses a positive sentiment. |
| 🔴 **Negative** | The text expresses a negative sentiment. |

Every prediction is accompanied by a confidence score.

---

# 📌 Example Use Cases

The platform can be used for:

* 🎬 Movie and product review analysis
* 💬 Social media sentiment analysis
* 🛍️ Customer feedback analysis
* 📢 Opinion mining
* 📊 Text classification
* 🧑‍💻 NLP experimentation
* 🤖 AI-powered feedback systems

---

# 🚀 Project Highlights

```text
✓ Fine-Tuned BERT Transformer
✓ PyTorch-Based Inference
✓ Hugging Face Model Hosting
✓ Flask REST API
✓ JavaScript Frontend
✓ Streamlit Dashboard
✓ NLTK Text Preprocessing
✓ Confidence-Based Predictions
✓ Dynamic Model Loading
✓ Modern Dark UI
✓ Prediction History
✓ Production-Oriented Project Structure
```

---

# 📜 License & Acknowledgments

The trained model weights are hosted as an open-source resource on **Hugging Face**.

Built with:

**Python · PyTorch · Transformers · NLTK · Flask · Streamlit · JavaScript**

---

<div align="center">

## 🎭 Sentiment Intelligence — BERT

### **THINK BIG. BUILD SMART.**

**Developed by Sudheer**

[GitHub](https://github.com/M-Sudheer18) · [Hugging Face](https://huggingface.co/Sudheer17/Sentiment)

</div>
