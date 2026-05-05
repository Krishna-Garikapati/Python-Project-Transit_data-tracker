# Transit Data Tracker (Python)

A Python-based application that fetches and processes real-time transit data from an API, with CSV fallback support. The project demonstrates API integration, JSON parsing, data transformation, filtering, and modular design.

---

# Features

-  Fetch transit data from external API
-  Load data from CSV (fallback option)
-  Parse and clean raw data
-  Extract key fields:
  - Bus ID
  - Route ID
  - Latitude & Longitude
-  Filter routes by user-defined range
-  Error handling for API failures and invalid data
- Modular project structure

---

# Project Structure
transit-tracker/
│
├── main.py
├── services/
│ └── api_service.py
├── utils/
│ └── parser.py
├── data/
│ └── sample.csv
└── README.md

# Installation
Clone the repository.
Eg: git clone https://github.com/your-username/transit-tracker.git
cd transit-tracker

# Key Concepts / Skills
- API integration
- JSON parsing
- CSV handling
- Error handling
- Modular design

# Usage
Run the application
1. Load data from transit API
2. Load data from CSV

# Author
Krishna Priyanka Garikapati
Halifax, NS