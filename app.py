import json
from flask import Flask, render_template

app = Flask(__name__)
with open('server.env', 'r') as r:
    env = json.loads(r.read())

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=env['is_debug'])