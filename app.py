from flask import Flask

app = Flask(__name__)

def get_greeting():
    return "Hello, CI/CD World!"

@app.route('/')
def hello():
    return get_greeting()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
