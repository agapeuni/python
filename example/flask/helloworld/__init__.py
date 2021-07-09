from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/info')
def greet():
    user = {'name': 'OneWay', 'age': "28"}
    return '''
<html>
    <head>
        <title>Name</title>
    </head>
    <body>
        <h1>Hello, ''' + user['name'] + '''!</h1>
        <h2>you’re ''' + user['age'] + ''' years old.</h2>
    </body>
</html>'''


@app.route('/hello')
def hello():
    return render_template('index.html', name="OneWay")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)
