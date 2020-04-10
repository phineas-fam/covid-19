from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config["SECRET_KEY"] = "5hir34yr7873489ry9fhu9ruf9r8f"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///backend.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False

CORS(app)
ma = Marshmallow(app)

from covidBE.models import db  # noqa isort:skip

db.init_app(app)

from covidBE.views import api_blueprint  # noqa isort:skip

app.register_blueprint(api_blueprint)
