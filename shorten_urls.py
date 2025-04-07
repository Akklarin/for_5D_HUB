from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

url_mapping = {}


def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.route('/', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url')
    if not original_url:
        return jsonify({"error": "URL is required"}), 400
    short_id = generate_short_url()
    url_mapping[short_id] = original_url
    return jsonify({"shortened_url": f"http://localhost:5000/{short_id}"}), 201


@app.route('/<short_id>', methods=['GET'])
def redirect_to_url(short_id):
    original_url = url_mapping.get(short_id)
    if not original_url:
        return jsonify({"error": "URL not found"}), 404
    return jsonify({"original_url": original_url}), 307


if __name__ == '__main__':
    app.run()
