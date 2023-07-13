from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap5


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
bootstrap = Bootstrap5(app)

from app import routes, util
