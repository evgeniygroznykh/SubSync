from flask import Flask
from flask_cors import CORS
from routes import BLUEPRINTS


app = Flask(__name__)
CORS(app)

for bp in BLUEPRINTS:
    app.register_blueprint(bp)
app.run(debug=True, port=8001)