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


@app.route("/board/<article_id>")
@app.route("/board", defaults={"article_id": 10})
def board_idx(article_id):
    print(article_id)
    return "{}번 게시물을 보고 계십니다.".format(article_id)


@app.route("/board", redirect_to="/new_board")
def board():
    print("board")
    return "/board URL을 호출하셨는데 실행이 안될겁니다"


@app.route("/new_board")
def new_board():
    return "/new_board URL이 호출되었습니다."


@app.route("/board/<id>/<id2>", redirect_to=redirect_new_board)
def board(id, id2):
    return "호출되지 않을 것입니다"


def redirect_new_board(adapter, id, id2):
    return "/new_board/{0}/{1}".format(id, id2)


@app.route("/new_board/<id>/<id2>")
def new_board(id, id2):
    return "{0}, {1} 변수와 함께 new_board URL이 호출되었습니다".format(id, id2)


@app.before_first_request
def before_first_request():
    # 앱이 기동되고 나서 첫번째 HTTP 요청에만 응답합니다.
    print(">1 before_first_request")


@app.before_request
def before_request():
    # 매 HTTP 요청이 처리되기 전에 실행
    print(">2 before_request")


@app.after_request
def after_request(response):
    # 매 HTTP 요청이 처리되고 나서 실행
    print(">3 after_request")
    return response


@app.teardown_request
def teardown_request(exception):
    # 매 HTTP 요청의 결과가 브라우저에 응답하고 나서 호출
    print(">4 teardown_request")


@app.teardown_appcontext
def teardown_appcontext(exception):
    # HTTP 요청의 애플리케이션 컨텍스트가 종료될때 실행
    print(">5 teardown_appcontext")
