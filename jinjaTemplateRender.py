from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')

app.run(debug=True)