from flask import Flask
from config import config
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(daemon=True)
scheduler.start()

def create_all(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .convert import convert as convert_blueprint
    app.register_blueprint(convert_blueprint, url_prefix='/convert')

    from .make_gif import make_gif as make_gif_blueprint
    app.register_blueprint(make_gif_blueprint, url_prefix='/make_gif')

    from .info_about_format import info_about_format as info_about_format_blueprint
    app.register_blueprint(info_about_format_blueprint, url_prefix='/info_about_format')

    from .info_about_image import info_about_image as info_about_image_blueprint
    app.register_blueprint(info_about_image_blueprint, url_prefix='/info_about_image')

    return app
