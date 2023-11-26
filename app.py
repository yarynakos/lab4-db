from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost/ajax'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from controllers import country_controller

app.register_blueprint(country_controller.country, url_prefix='/countries')

if __name__ == '__main__':
    app.run()
