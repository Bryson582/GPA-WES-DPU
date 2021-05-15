import os

basedir = os.path.abspath(os.path.dirname(__file__))
picFolder = os.path.join('static','pic')

class Config(object):

    # APP MODE
    DEBUG = True

    # Top secret of website
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6LfHloUaAAAAAOdFT9acPtpPj7Vg1NWKkRjQcgZw'

    # Database configuration
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:19951979kbL@localhost:3306/test'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Recaptcha

    RECAPTCHA_PUBLIC_KEY = '6Lc6bo8aAAAAAJhh3qH37oe1F4uryHSF94PIv2vr'
    RECAPTCHA_PRIVATE_KEY = '6Lc6bo8aAAAAAFJKKASmd67YuBkigrZjRP4Yz7Jm'

    # Image
    UPLOAD_FOLDER =picFolder




