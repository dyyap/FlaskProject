from flask import Flask, render_template
import psutil
from flaskwebgui import FlaskUI

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/api/cpu')
def api():
    return str(psutil.cpu_percent(interval=0.1))

if __name__ == "__main__":
    #app.run(debug = True)
    #gui.run()
    FlaskUI(app=app, server="flask").run()