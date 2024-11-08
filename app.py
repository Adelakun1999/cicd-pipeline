from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from my ci/cd powered flask app! V2'

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
