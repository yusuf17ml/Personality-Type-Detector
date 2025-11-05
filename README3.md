## Introduction

This project predicts an individual's personality type (introvert, extrovert, or ambivert) based on their behavioral and psychological characteristics. The primary use case is to provide a data-driven assessment of personality traits, offering insights beyond self-reported questionnaires.

This project offers several key benefits. First, it provides an objective, data-driven classification. Second, it leverages machine learning techniques to analyze complex behavioral patterns. Finally, the project is implemented in a Jupyter Notebook environment, facilitating ease of use and modification.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

*   Predict your personality type (Introvert, Extrovert, or Ambivert) based on provided data.
*   Analyze behavioral and psychological characteristics.
*   Evaluate traits such as social energy, online social usage, and friendliness.
*   Classify individuals using a trained machine learning model.

## Tech Stack

This project leverages the following technologies:

*   **Programming Language:**
    *   Python 3.x
*   **Data Science Libraries:**
    *   pandas: 2.0.3
    *   scikit-learn: 1.3.0
    *   NumPy: 1.25.2
*   **Notebook Environment:**
    *   Jupyter Notebook
*   **Visualization:**
    *   matplotlib: 3.7.2
    *   seaborn: 0.12.2

## Prerequisites

To successfully run this project, ensure you have the following prerequisites installed and configured:

**Required:**

*   **Python:** Version 3.7 or higher. Verify your Python installation with:

    ```bash
    python --version
    ```

*   **Jupyter Notebook:** Install using pip:

    ```bash
    pip install notebook
    ```

*   **Essential Python Libraries:** Install the following libraries using pip:

    ```bash
    pip install pandas scikit-learn matplotlib seaborn
    ```

**Optional:**

*   **Git:** For cloning the repository. Ensure Git is installed and accessible in your system's PATH. Verify with:

    ```bash
    git --version
    ```

## Installation

To set up the Personality Type Detector project, follow these steps:

1.  Clone the repository using Git.

    ```bash
    git clone https://github.com/yusuf17ml/Personality-Type-Detector.git
    ```

2.  Navigate into the project directory.

    ```bash
    cd Personality-Type-Detector
    ```

3.  Create a virtual environment to manage project dependencies.

    ```bash
    python -m venv .venv
    ```

4.  Activate the virtual environment.

    *   **Linux/macOS:**

        ```bash
        source .venv/bin/activate
        ```

    *   **Windows:**

        ```bash
        .venv\Scripts\activate
        ```

5.  Install the required Python packages.

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the personality type detection application, execute the FastAPI server.

1.  **Start the FastAPI Server:**

    Navigate to the project's root directory in your terminal and run the following command:

    ```bash
    uvicorn app.main:app --reload
    ```

    This command starts the FastAPI server, enabling automatic code reloading for development. Ensure you have installed the necessary dependencies listed in `requirements.txt`.

2.  **Using the Prediction Endpoint:**

    The application exposes a prediction endpoint at `/predict`. You can send a POST request to this endpoint with a JSON payload containing the input features.

    **Example Input Data (JSON):**

    ```json
    {
        "social_energy": 7,
        "alone_time_preference": 3,
        "talkativeness": 6,
        "deep_reflection": 8,
        "group_comfort": 7,
        "party_liking": 5,
        "listening_skill": 9,
        "empathy": 8,
        "creativity": 7,
        "organization": 6,
        "leadership": 7,
        "risk_taking": 5,
        "public_speaking_comfort": 6,
        "curiosity": 8,
        "routine_preference": 4,
        "excitement_seeking": 6,
        "friendliness": 9,
        "emotional_stability": 8,
        "planning": 7,
        "spontaneity": 5,
        "adventurousness": 6,
        "reading_habit": 7,
        "sports_interest": 4
    }
    ```

    **Code Example (Python using `requests`):**

    ```python
    import requests
    import json

    url = "http://127.0.0.1:8000/predict"  # Replace with your server address if different
    headers = {"Content-Type": "application/json"}
    data = {
        "social_energy": 7,
        "alone_time_preference": 3,
        "talkativeness": 6,
        "deep_reflection": 8,
        "group_comfort": 7,
        "party_liking": 5,
        "listening_skill": 9,
        "empathy": 8,
        "creativity": 7,
        "organization": 6,
        "leadership": 7,
        "risk_taking": 5,
        "public_speaking_comfort": 6,
        "curiosity": 8,
        "routine_preference": 4,
        "excitement_seeking": 6,
        "friendliness": 9,
        "emotional_stability": 8,
        "planning": 7,
        "spontaneity": 5,
        "adventurousness": 6,
        "reading_habit": 7,
        "sports_interest": 4
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        prediction = response.json()
        print(f"Predicted Personality Type: {prediction['personality_type']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    ```

    **Expected Output:**

    ```
    Predicted Personality Type: Extrovert
    ```

3.  **Using the Streamlit Frontend:**

    The project includes a Streamlit frontend for easier interaction.

    **Run the Streamlit Application:**

    From the project's root directory, execute:

    ```bash
    streamlit run frontend/app.py
    ```

    This command launches the Streamlit application in your web browser.  The frontend provides an interactive interface to input features and receive personality type predictions.

## Contributing

This project welcomes contributions. Review the guidelines below to contribute effectively.

## License

This project is not licensed.