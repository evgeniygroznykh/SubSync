from flask import Flask
from flask_cors import CORS
from routes import ROUTE_BLUEPRINTS
from views.tasks import TASKS
from setup import register_blueprints, run_scheduler



app = Flask(__name__)
CORS(app)

register_blueprints(ROUTE_BLUEPRINTS, app)
run_scheduler(TASKS)

app.run(port=8001)