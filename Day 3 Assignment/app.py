from flask import Flask, render_template
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from model import User, Board

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:RIVERHOME@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# API config
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


from routes.user import user_blp
from routes.board import board_blp

api = Api(app)
api.register_blueprint(user_blp)
api.register_blueprint(board_blp)

@app.route('/manage-board')
def manage_board():
    return render_template('board.html')

@app.route('/manage-user')
def manage_user():
    return render_template('user.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
