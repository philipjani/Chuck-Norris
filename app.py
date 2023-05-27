from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    r = json.loads(r.text)
    r = r['value']
    return render_template('index.html', data=r)

if __name__ == '__main__':
    app.run(debug=True)