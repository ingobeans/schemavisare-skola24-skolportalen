from flask import Flask,render_template,request
from . import clam
import datetime, uuid

app = Flask(__name__)

sessions = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/session", methods=["POST"])
def session():
    data = request.json
    session_uuid = str(uuid.uuid4())
    skolportal_session = clam.SkolportalSession(data["username"], data["password"])
    skola24_session = clam.Skola24Session(skolportal_session)
    sessions[session_uuid] = skola24_session
    return session_uuid

@app.route("/timetable", methods=["POST"])
def timetable():
    data = request.json
    session = sessions[data["session"]]
    today = datetime.date.today()
    week = today.isocalendar()[1]
    if today.weekday() in [5, 6]:
        week += 1
    return session.get_timetable(week, int(data["width"]), 650, 0)

if __name__ == '__main__':
    app.run(debug=True)
