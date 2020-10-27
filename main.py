from flask import Flask,render_template, request, make_response, Response, redirect
import sqlite3
import json

app = Flask(__name__)



# SQLite3 Connection
conn = sqlite3.connect('data.db', check_same_thread=False)
curs = conn.cursor()


#track car Page
@app.route("/")
def track():
    return render_template('tracker.html')


#Location Data
@app.route('/locationdata', methods=["GET", "POST"])
def locationdata():
    for row in curs.execute("SELECT * FROM map ORDER BY timestamp DESC LIMIT 1"):
        longi = row[1]
        lati = row[2]
    Longitude = longi
    Latitude = lati
    data = {"geometry":{"type":"Point","coordinates":[Latitude, Longitude]},"type":"Feature","properties":{}}
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True)
