from flask import Flask
from config import Config

PORT_NUMBER = 8000

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
app.run(host='0.0.0.0', port=PORT_NUMBER)
