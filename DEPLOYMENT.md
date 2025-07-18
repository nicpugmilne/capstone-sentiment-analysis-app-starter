# Deployment Guide

## Deploying to Render

### 1. Build Command

```
pip install --upgrade pip && pip install -r requirements.txt
```

### 2. Start Command

```
gunicorn app:app
```

### 3. Environment Variables

Set the following environment variable in Render:

- **PYTHON_VERSION**: `3.10.12`

### 4. Important Notes

- Render automatically spins down free web services after 15 minutes of inactivity
- The first request after inactivity may take a few seconds to a couple of minutes to respond
- This is normal behavior for free tier deployments

## Local Development

### Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Run Tests

```bash
python -m pytest tests/tests.py -v
```

## Features Implemented

✅ **US-01**: VADER sentiment analysis integration
✅ **US-02**: Custom Keras model training with UCI dataset
✅ **US-03**: Model testing and validation
✅ **US-04**: Custom model integration in Flask app
✅ **US-05**: Modern, responsive UI design
✅ **US-06**: Ready for deployment

## Model Performance

- Custom model accuracy: 79.7%
- Trained on 2,748 samples from Yelp, Amazon, and IMDB datasets
- Supports both VADER and custom model sentiment analysis
