import json


def load_db():
    with open("Data.json") as json_file:
        data = json.load(json_file)
        return data


def save_db(db):
    try:
        db = json.loads(db)
        with open("Data.json", 'w') as f:
            return json.dump(db, f)
    except json.decoder.JSONDecodeError as e:
        return 1


db = load_db()

