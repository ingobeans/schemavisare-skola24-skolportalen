from flask import Flask,render_template,request
from . import clam
import datetime, pytz

app = Flask(__name__)

sessions = {}

class Session:
    def __init__(self,username,password) -> None:
        self.skola24_session = create_skola24_session(username, password)
        self.expires = self.skola24_session.get_info()["sessionExpires"]
        print(self.expires)
        print("init new session")

@app.route("/")
def home():
    return render_template("index.html")

def create_skola24_session(username, password):
    skolportal_session = clam.SkolportalSession(username, password)
    skola24_session = clam.Skola24Session(skolportal_session)
    return skola24_session

def generate_session_id(username, password):
    return username+"|"+password

def get_session(username, password):
    session_id = generate_session_id(username, password)
    session: Session = sessions.get(session_id)
    print(f"looking for a {username} session")
    
    if not session:
        print(f"no {username} session exists, creating one")
        session = Session(username, password)
        sessions[session_id] = session
    else:
        session_expires_datetime = datetime.datetime.fromisoformat(session.expires)
        
        if session_expires_datetime.tzinfo is None:
            session_expires_datetime = session_expires_datetime.replace(tzinfo=datetime.timezone.utc)
        
        current_time = datetime.datetime.now(session_expires_datetime.tzinfo)
        
        if current_time > session_expires_datetime:
            print(f"session {username} is too old, creating new one")
            session = Session(username, password)
            sessions[session_id] = session
        else:
            # calc the remaining time until expiration
            time_remaining = session_expires_datetime - current_time
            minutes_remaining = time_remaining.total_seconds() / 60
            print(f"Time remaining until expiration: {minutes_remaining:.2f} minutes")
    
    print(f"returning {username} session")
    return session.skola24_session

@app.route("/timetable", methods=["POST"])
def timetable():
    data = request.json
    session = get_session(data["username"],data["password"])
    today = datetime.date.today()
    week = today.isocalendar()[1]
    if today.weekday() in [5, 6]:
        week += 1
    print("getting timetable")
    return session.get_timetable(week, int(data["width"]), 650, 0, datetime.datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)
