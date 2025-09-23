from flask import Flask
from flask_smorest import Api
from api import blp
# Flask용 REST API 확장 라이브러리(open API와 Swagger 지원)
# GET, POST, PUT, DELETE을 받을 수 있는 서버를 만듦.

app = Flask(__name__)

#swagger/OpenAPI 문서에서 사용할 문자열
app.config['API_TITLE'] = 'Books API'
#api 버전지정, 문서 및 서비스 버전관리시 사용됨
app.config['API_VERSION'] = 'v1'
#open API 스펙 버전 3.0.2가 일반적임
app.config['OPENAPI_VERSION'] = '3.0.2'
# Open API 스팩 (Json)이 제공될 라우크의 접두어를 지정 '/'가 기본값
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_URL'] = '/swagger/'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)
api.register_blueprint(blp)
#book_blp라는 블루프린트를 API에 등록한다. 블루프린트는 API 엔드포인트 묶음을 담당. 실제 상세 기능 구현은 해당 블루프린트에 들어감.


if __name__ == '__main__':
    app.run(debug=True)
