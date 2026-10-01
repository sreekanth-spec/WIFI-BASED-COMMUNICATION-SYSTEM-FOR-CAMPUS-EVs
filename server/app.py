from flask import Flask, request, jsonify, render_template
import datetime

app = Flask(__name__)

ev_fleet = {"EV_01": {"status": "IDLE", "zone": "Zone_A"}, "EV_02": {"status": "IDLE", "zone": "Zone_B"}}
stop_zones = {"STOP_A": "Zone_A", "STOP_B": "Zone_B"}
pending_requests = []

@app.route('/')
def dashboard():
    return render_template('index.html', evs=ev_fleet, requests=pending_requests)

@app.route('/api/request', methods=['POST'])
def handle_request():
    ev_fleet["EV_01"]["status"] = "BUSY"
    pending_requests.append({"timestamp": "Just now", "stop_id": request.json.get("stop_id"), "assigned_ev": "EV_01"})
    return jsonify({"assigned_ev": "EV_01", "status": "SUCCESS"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)