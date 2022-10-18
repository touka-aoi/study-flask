from flask import Flask, render_template
import pandas as pd

df = pd.read_csv("./data/Boston.csv")

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", tables=[df.to_html(classes='data')])