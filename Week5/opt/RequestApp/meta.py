import flask

app = flask.Flask(__name__)
app.secret_key = "Sekr3t_Tok3n"
app.config.update(
    SESSION_COOKIE_SAMESITE='Strict',
)

