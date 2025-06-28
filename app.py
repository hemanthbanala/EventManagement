from flask import Flask, request, jsonify
import json
from datetime import datetime, timedelta
import threading

app = Flask(__name__)

EVENTS_FILE = "events.json"

# Load events from file
def load_events():
    try:
        with open(EVENTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save events to file
def save_events(events):
    with open(EVENTS_FILE, "w") as file:
        json.dump(events, file)

# Get events due within the next hour
def get_upcoming_reminders():
    now = datetime.now()
    upcoming = []
    for event in load_events():
        start_time = datetime.strptime(event["start_time"], "%Y-%m-%d %H:%M:%S")
        if now <= start_time <= now + timedelta(hours=1):
            upcoming.append(event)
    return upcoming

# Background thread for reminders
def reminder_thread():
    while True:
        reminders = get_upcoming_reminders()
        for event in reminders:
            print(f"Reminder: {event['title']} is starting at {event['start_time']}")
        threading.Event().wait(60)

threading.Thread(target=reminder_thread, daemon=True).start()

@app.route("/events", methods=["POST"])
def create_event():
    event = request.json
    events = load_events()
    events.append(event)
    save_events(events)
    return jsonify({"message": "Event created successfully!"}), 201

@app.route("/events", methods=["GET"])
def list_events():
    events = sorted(load_events(), key=lambda x: x["start_time"])
    return jsonify(events)

@app.route("/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    events = load_events()
    if 0 <= event_id < len(events):
        events[event_id].update(request.json)
        save_events(events)
        return jsonify({"message": "Event updated successfully!"})
    return jsonify({"error": "Event not found"}), 404

@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    events = load_events()
    if 0 <= event_id < len(events):
        events.pop(event_id)
        save_events(events)
        return jsonify({"message": "Event deleted successfully!"})
    return jsonify({"error": "Event not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)