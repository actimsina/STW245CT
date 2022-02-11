"""
Meta Class to create the flask app, and avoid circular imports
"""

import flask
from flask_redis import FlaskRedis
from jinja_markdown import MarkdownExtension


REDIS_URL = "redis://redis:6379/0"
SECRET_KEY = b"foobarbaz"

app = flask.Flask(__name__)
app.config.update(
    REDIS_URL = REDIS_URL,
    #SESSION_TYPE= "redis",
    #SESSION_REDIS = redis.from_url(REDIS_URL),
    SESSION_COOKIE_SAMESITE='Strict',
    )

app.config["SECRET_KEY"] = SECRET_KEY

app.jinja_env.add_extension(MarkdownExtension)

redis_client = FlaskRedis(app)


