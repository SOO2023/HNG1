# HNG12 Stage 1 Backend Task  

## Project Overview  
This is a simple public API developed for the HNG12 internship Stage 1 backend task. The API provides mathematical properties about a number, properties such as:  

- if the number is a prime number 
- if the number is a perfect number 
- if the number is a odd, even, or armstrong number 
- one fun fact about the number

## API Documentation  

### Endpoint  
**GET** `https://hng1-3h1g.onrender.com/api/classify-number?number=<number>`

### Response Format  
The API returns a JSON response with the following structure:  

```json
{
    "number": 0,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["string"],
    "digit_sum": 0,
    "fun_fact": "string"
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

### 4: Environment Variables

To set up environment variables, create a copy of the `.env-example` file and rename it to `.env`:

```bash
cp .env-example .env
```

### 5: Start the FastAPI Application with Uvicorn
Run the FastAPI application using Uvicorn.

```bash
uvicorn app.main:app --port 8000
```

### 5: Test the API
Open a browser and make a GET request to: `http://127.0.0.1:8000/api/classify-number`

## Additional Resources

- Official FastAPI Documentation: https://fastapi.tiangolo.com/
- Learn More About Python Backend Developers: https://hng.tech/hire/python-developers

## Author

Samson Olaide
GitHub: https://github.com/SOO2023