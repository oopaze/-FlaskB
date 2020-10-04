from app import app
from app.models.tables import * 


@app.route("/")
def index():
    return "Hello world! "