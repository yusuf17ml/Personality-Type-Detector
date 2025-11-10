# Use the latest Python image from Docker Hub (Python 3.11)
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies in the container
RUN pip install --no-cache-dir --timeout=1000 -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Expose the FastAPI and Streamlit ports
EXPOSE 8000 8501

# Run FastAPI with Uvicorn and Streamlit simultaneously
CMD ["sh", "-c", "uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend/app.py --server.port 8501"]
