from flask import Flask, render_template
from flask import Response, make_response

app = Flask(__name__)
app.debug = True

app.config.update(
    DEBUG=True
)


@app.route('/')
def index():
    return render_template('index.html', name="OneWay")


@app.route("/hello")
def helloworld():
    return 'Hello, World!'


@app.route("/res1")
def res1():
    custom_response = Response("Custom Response", '200 OK', {
        "Program": "Flask Web Application"
    })

    return make_response(custom_response)


@app.route("/res2")
def res2():
    return make_response("Custom Response")


@app.route("/res3")
def res3():
    return make_response(('Tuple Custom Response', 'OK', {
        'response_method': 'Tuple Response'
    }))


@app.route('/name1')
def name1():
    user = {'name': 'OneWay', 'age': "48"}
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


@app.route("/board/<article_id>")
@app.route("/board", defaults={"article_id": 10})
def board_idx(article_id):
    return "{}번 게시물을 보고 계십니다.".format(article_id)


@app.route("/board", redirect_to="/new_board")
def board():
    return "/board URL을 호출하셨는데 실행이 안될겁니다"


@app.route("/new_board")
def new_board():
    return "/new_board URL이 호출되었습니다."
