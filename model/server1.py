from flask import Flask, request, jsonify
import server

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': server.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response




if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    server.load_saved_artifacts()
    app.run()
