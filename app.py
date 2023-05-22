from flask import Flask
from flask_cors import CORS
from routes.file import file_route

app = Flask(__name__)
app.register_blueprint(file_route)

CORS(app)

app.run(debug=True)