from flask import Flask

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# ...

# from app.errors import bp as errors_bp
# app.register_blueprint(errors_bp)

# ...

from app import routes, models
