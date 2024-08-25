from flask import Flask,render_template,request
import clam, datetime, uuid

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
    return session.get_timetable(datetime.date.today().isocalendar()[1], int(data["width"]), 650, 0)

app.run(debug=True,port=6969)