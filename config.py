import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MAX_CONTENT_LENGTH = 4096 * 4096
    UPLOAD_EXTENSIONS = ['.jpg', '.png', 'gif']
    UPLOAD_PATH = 'uploads'