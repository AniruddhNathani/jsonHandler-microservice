from flask import Flask, render_template, jsonify, request
import json
import pandas as pd
from model import save_db, load_db


app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def index_post():
    db = request.form["myText"]
    if save_db(db) == 1:
        return render_template("error.html")

    with open('Data.json') as json_file:
        data = json.load(json_file)
    df = pd.DataFrame(data)
    df['index'] = df.reset_index().index
    grouped_df = df.groupby("name")["name", "duration"].sum().reset_index()
    count_df = df.groupby("name")["name"].count().reset_index(name="count")
    original_objects = df.to_json(orient='records')
    counted_objects = count_df.to_json(orient='records')
    grouped_objects = grouped_df.to_json(orient='records')
    return render_template("index.html", objects=original_objects, grouped=grouped_objects, count=counted_objects)


@app.route("/api/object/")
def api_object_list():
    db = load_db()
    return jsonify(db)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

