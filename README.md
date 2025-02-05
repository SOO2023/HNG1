# HNG12 Stage 0 Backend Task  

## Project Overview  
This is a simple public API developed for the HNG12 internship Stage 1 backend task. The API provides mathematical properties about a number, properties such as:  

- if the number is a prime number 
- if the number is a perfect number 
- if the number is a odd, even, or armstrong number 
- one fun fact about the number

## API Documentation  

### Endpoint  
**GET** `https://hng0-nvg7.onrender.com`

### Response Format  
The API returns a JSON response with the following structure:  

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^ = 371"
}
```

## Setup Instructions

### Prerequisites
Ensure you have the following installed:

- Python 3.x (or any other supported programming language)
- Git
- A hosting platform

## Running the Project Locally

### 1: Clone the project Repository

Clone the Repository
Clone your FastAPI backend project repository from GitHub or any other version control system.

```bash
git clone https://github.com/SOO2023/HNG1.git

cd HNG1
```

### 2: Create and Activate a Virtual Environment

Create a virtual environment for your project to isolate dependencies.

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### 3: Install Dependencies (For Python FastAPI)
```
pip install -r requirements.txt
```

### 4: Start the FastAPI Application with Uvicorn
Run the FastAPI application using Uvicorn.

```bash
uvicorn app.main:app --port 8000
```

### 5: Test the API
Open a browser and make a GET request to: `http://127.0.0.1:8000`

## Additional Resources

- Official FastAPI Documentation: https://fastapi.tiangolo.com/
- Learn More About Python Backend Developers: https://hng.tech/hire/python-developers

## Author

Samson Olaide
GitHub: https://github.com/SOO2023