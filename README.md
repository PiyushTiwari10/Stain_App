# Stain Detecture
FastAPI backend which would detect stain from the uploaded image.
The Model is built using CNN (Convolutional Neutral Network)

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. **Start the server:**
   ```bash
    fastapi run main.py
   ```

## Endpoints

* **[detect_stain]:**
- Accept Image
- Resize the image
- Convert Image to Array
- Predicts the type of stain
- Return response 
