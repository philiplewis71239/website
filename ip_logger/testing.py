from flask import request, jsonify, Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({'ip': request.environ["REMOTE_ADDR"]}), 200

app.run(
    debug=True,
    host="0.0.0.0"
)
