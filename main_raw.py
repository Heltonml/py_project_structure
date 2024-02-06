from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return jsonify({ "msg": "Server is running!!!" })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=None)
