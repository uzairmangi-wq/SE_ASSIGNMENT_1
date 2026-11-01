
from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# Generate three unique API keys
api_keys = {
    secrets.token_hex(16): "Consumer 1",
    secrets.token_hex(16): "Consumer 2",
    secrets.token_hex(16): "Consumer 3"
}


@app.route("/")
def home():
    return "RootSoftware Text Processing API is Running!"


# POST endpoint for text processing
@app.route("/process", methods=["POST"])
def process_text():

    # Get API key from request header
    api_key = request.headers.get("X-API-Key")

    # Validate API key
    if api_key not in api_keys:
        return jsonify({"error": "Invalid or missing API key"}), 401

    # Get text from JSON
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Text is required"}), 400

    text = data["text"]

    if not isinstance(text, str):
        return jsonify({"error": "Text must be a string"}), 400

    # Convert text into uppercase
    processed_text = text.upper()

    return jsonify({
        "consumer": api_keys[api_key],
        "original_text": text,
        "processed_text": processed_text
    })


if __name__ == "__main__":

    print("\nRootSoftware API Keys:")

    for key, consumer in api_keys.items():
        print(consumer + ": " + key)

    app.run(debug=True, port=5001)
