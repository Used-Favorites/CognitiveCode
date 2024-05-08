from flask import Flask
from src.middlewares import authData

from .router.main import main

app = Flask('CognitiveFlask')

app.register_blueprint(main)