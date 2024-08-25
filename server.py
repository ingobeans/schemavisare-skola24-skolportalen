from flask import Flask,render_template,request
import clam, datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/timetable", methods=["POST"])
def timetable():
    data = request.json
    print(f"receive: {data}")
    print(f"username: {repr(data['username'])}")
    print(f"password: {repr(data['password'])}")
    skolportal_session = clam.SkolportalSession(data["username"], data["password"])
    skola24_session = clam.Skola24Session(skolportal_session)
    return skola24_session.get_timetable(datetime.date.today().isocalendar()[1], int(data["width"]), 650, 0)

app.run(debug=True,port=6969)