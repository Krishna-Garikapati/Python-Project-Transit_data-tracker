
# Library used to make HTTP requests (call APIs)
import requests

URL = "https://prog2700.onrender.com/hrmbuses"

def fetch_transit_data():
    try:
        response = requests.get(URL, timeout=20)

        # Raises exception for HTTP errors (e.g., 404, 500)
        response.raise_for_status()

        # Converts JSON response → Python (list/dict)
        # Note: Data may still need cleaning (handled in parser.py),
        # such as missing values or type conversion (e.g., strings to numbers)
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return []

# api_service.py contains a function fetch_transit_data()
# This function calls the API and returns raw data in Python format
# (list/dictionary) for further processing

#This module is responsible for fetching raw data from an external API and returning it in Python format, while delegating data validation and transformation to a separate parser module.