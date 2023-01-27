from flask import Flask, render_template, abort
from email import message
from werkzeug.exceptions import HTTPException
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# @app.errorhandler(404)
# @app.errorhandler(500)
# def handleError(err):
#     return render_template("message.html", title=err.name, message=err.description), err.code

@app.errorhandler(HTTPException)
def handleError(err):
    return render_template("message.html", title=err.name, message=err.description), err.code
@app.route('/simulate500')
def simulate500():
    return abort(500)

@app.route('/simulate501')
def simulate501():
    return abort(501)

if __name__ == '__main__':
    app.run(debug=True)
