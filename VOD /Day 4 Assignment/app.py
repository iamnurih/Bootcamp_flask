from flask import Flask
from flask_smorest import Api
from posts_routes import create_post_blueprint
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:RIVERHOME@localhost:3306/blog_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

db.init_app(app)
api = Api(app)
posts_blp = create_post_blueprint(db)
api.register_blueprint(posts_blp)

if __name__ == '__main__':
    app.run(debug=True)
