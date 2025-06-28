# Event Management REST API

This project is a simple Event Management REST API built with Python 3.x and Flask.

## Requirements
- Python 3.x
- Flask

## Setup Instructions
1. **Install Python 3.x**
   - Download from https://www.python.org/downloads/
2. **Install dependencies**
   - Open a terminal in the project directory and run:
     ```
     pip install flask
     ```
3. **Run the application**
   - In the terminal, run:
     ```
     python app.py
     ```
   - The server will start, usually at `http://127.0.0.1:5000/`

## Example API Commands

### Get all events
```
curl http://127.0.0.1:5000/events
```
**Output:**
```
[
  {
    "title": "Team Meeting",
    "description": "Discuss project updates and next steps",
    "start_time": "2025-06-28 15:00:00",
    "end_time": "2025-06-28 16:00:00"
  }
]
```

### Add a new event
```
curl -X POST http://127.0.0.1:5000/events -H "Content-Type: application/json" -d '{"title": "Workshop", "description": "Python workshop", "start_time": "2025-07-01 10:00:00", "end_time": "2025-07-01 12:00:00"}'
```
**Output:**
```
{"message": "Event added successfully"}
```
