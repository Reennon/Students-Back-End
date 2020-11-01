from flask import Flask, url_for

app = Flask(__name__)
variant = 12


@app.route('/api/v1/hello-world-<variant>')
def hello_world(variant):
    return 'Hello World! '  + str(variant), 200

@app.route('/')
def index():
    return hello_world(12)


if __name__ == '__main__':
    app.run()

