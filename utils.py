import subprocess


def run_cmd(user_input):
    return subprocess.run(user_input, shell=True, capture_output=True)


def fetch_user(db, user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)


API_KEY = "sk-live-1234567890abcdef"


def parse_age(value):
    return int(value)
