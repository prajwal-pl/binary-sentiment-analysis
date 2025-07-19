# Binary Sentiment Analysis

A sentiment analysis application that classifies text as positive or negative using a fine-tuned transformer model.

## Project Overview

This project consists of two main components:

1. **Backend**: A Flask API that serves a fine-tuned BERT model for sentiment analysis
2. **Frontend**: A React application with TypeScript and Vite that provides a user interface for sentiment analysis

## Technology Stack

### Backend

- Python 3.12
- Flask
- Transformers (Hugging Face)
- PyTorch
- Docker

### Frontend

- React 18
- TypeScript
- Vite
- Tailwind CSS
- Shadcn UI
- Docker

## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- Git

### Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/prajwal-pl/binary-sentiment-analysis.git
   cd binary-sentiment-analysis
   ```

2. Start the application using Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. Once the containers are up and running, access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000

## API Endpoints

The backend provides the following API endpoints:

- `POST /predict`: Analyzes the sentiment of provided text
  - Request body: `{ "text": "Your text here" }`
  - Response: `{ "label": "positive" or "negative", "score": 0.XX }`

## Project Structure

```
binary-sentiment-analysis/
├── backend/
│   ├── controllers/       # API controllers
│   ├── model/             # Pre-trained sentiment analysis model
│   ├── results/           # Checkpoints from model fine-tuning
│   ├── data.jsonl         # Training data
│   ├── finetune.py        # Script for fine-tuning the model
│   ├── main.py            # Flask application entry point
│   ├── Dockerfile         # Backend Docker configuration
│   └── requirements.txt   # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── lib/           # Utility functions and API client
│   │   └── ...            # Other frontend files
│   ├── Dockerfile         # Frontend Docker configuration
│   └── package.json       # Frontend dependencies
└── docker-compose.yml     # Docker Compose configuration
```

## Development

### Backend Development

To run the backend locally without Docker:

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python main.py
   ```

### Frontend Development

To run the frontend locally without Docker:

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## Model Information

The sentiment analysis model is a fine-tuned BERT model trained on a custom dataset. The model was fine-tuned using the Hugging Face Transformers library.

## Finetune script

You can use fine tuning by running `python finetune.py`
