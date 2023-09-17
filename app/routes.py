from app import app

@app.route("/")
@app.route("/feed")
def index():
    return "Hello, World! from Miguel"