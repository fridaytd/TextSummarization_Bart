from flask import Flask, request, jsonify
from flask_cors import CORS
from app.summarizer import Summarizer


def create_app():

    summarizer = Summarizer()

    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def main():
        return "Main"

    @app.post('/sum')
    def sum():
        data = request.get_json()
        try:
            input = data['document']
            output = summarizer.inference(input)
            return jsonify({
                "summary": output
            }), 200
        except Exception as ex:
            print(ex)
            return jsonify({
                "error": str(ex),
            }), 500

    app.run(debug=True)
