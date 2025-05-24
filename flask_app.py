# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import os

app = Flask(__name__)

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db = os.getenv("DB")

print(f"Env printing: host->{host},user->{user},password->{password},db->{db}")


@app.route('/')
def hello_world():
    return 'Hello from Flask!'
