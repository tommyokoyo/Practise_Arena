#!flask/bin/python

from flask import Flask, jsonify, abort, make_response, request
from PayloadEncryption.aesEncryption import encryptGCM, decryptGCM

app = Flask(__name__)

# Check api status
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({'status': 'ok'})

# check aes status
@app.route('/aes/status', methods=['POST'])
def get_aes_status():
    my_password = 'my_very_secure_password'
    data = request.json.get('payload')
    print(data)
    print(decryptGCM(data, my_password))
    if not data:
        abort(400)
    return jsonify({'status': 'ok'})

# error handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)