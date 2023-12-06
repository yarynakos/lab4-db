from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost/ajax'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from controllers import country_controller, city_controller, access_controlers, object_controller, user_controller, \
    zone_controller, room_controller, sensor_controller, schedule_controller, notification_controller

app.register_blueprint(country_controller.country, url_prefix='/countries')
app.register_blueprint(city_controller.city, url_prefix='/cities')
app.register_blueprint(access_controlers.access_level, url_prefix='/access')
app.register_blueprint(object_controller.object, url_prefix='/object')
app.register_blueprint(user_controller.user, url_prefix='/user')
app.register_blueprint(zone_controller.zone, url_prefix='/zone')
app.register_blueprint(room_controller.room, url_prefix='/room')
app.register_blueprint(sensor_controller.sensor, url_prefix='/sensor')
app.register_blueprint(schedule_controller.schedule, url_prefix='/schedule')
app.register_blueprint(notification_controller.notification, url_prefix='/notification')


if __name__ == '__main__':
    app.run()
