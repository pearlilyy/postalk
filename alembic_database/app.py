from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_postalk():
    return 'Hello, Postalk Users - Docker in VS Code!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
