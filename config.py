import os

UPLOAD_FOLDER = os.getcwd() + '/static/users_images'


class Config:
    SECRET_KEY = 'ipidoras'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    UPLOAD_FOLDER = UPLOAD_FOLDER
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    SSL_REDIRECT = True if os.environ.get('DYNO') else False

    @staticmethod
    def init_app(app):
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


config = {
    'default': Config
}
