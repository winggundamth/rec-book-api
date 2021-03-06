import os
from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', default='config.DevelopmentConfig'))

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
