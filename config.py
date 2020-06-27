import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADS_DEFAULT_DEST = os.path.join(BASE_DIR, 'app/static/photos/')

    UPLOADED_IMAGES_DEST = os.path.join(BASE_DIR, 'app/static/photos/')

    SUB_DIR = os.path.join(BASE_DIR, 'app/static/photos')

    SECRET_KEY = 'sddkgfbkdsjnjkdjdsjek'

    SQLALCHEMY_RECORD_QUERIES = True

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
