from flask import Flask
from routes import routes_blueprint

app = Flask(__name__)
app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)