from flask import Flask, request, render_template, redirect
from flask import Response, make_response, session

app = Flask(__name__)
app.debug = True
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
app.config.update(DEBUG=True)
app.config.update(MAX_CONTENT_LENGTH=1024*1024*10)


@app.route('/')
def index():
    return render_template('index.html', name="OneWay")


@app.route("/example/max_content_len", methods=["GET"])
def example_content_length():
    print(request.max_content_length)
    return ""


@app.route("/session_set")
def session_set():
    session['ID'] = 'JPUB Flask Session Setting'
    return "세션이 설정되었습니다"


@app.route("/session_out")
def session_out():
    del session['ID']
    return "세션이 제거되었습니다."


@app.route("/cookie_set")
def cookie_set():
    custom_resp = Response("Cookie를 설정합니다")
    custom_resp.set_cookie("ID", "JPUB Flask Programming")

    return custom_resp


@app.route("/cookie_out")
def cookie_out():
    custom_resp = Response("Cookie를 종료합니다")
    custom_resp.set_cookie("ID", expires=0)

    return custom_resp


@app.route("/cookie_status")
def cookie_status():
    return "ID 쿠키는 %s 값을 가지고 있습니다" % request.cookies.get('ID', '빈 문자열')


"""
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
"""
