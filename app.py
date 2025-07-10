from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
import google.generativeai as genai

genai.configure(api_key="AIzaSyDrar3z7uSLxHSIk1homX4wa6RRUGe1DIE")
model = genai.GenerativeModel("gemini-1.5-flash")



# Route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # Simulate fetching and summarizing content
        # Replace this with actual logic to fetch and summarize content
        response = model.generate_content(f"Summarize the following URL in detail  for exam preparation: {url}")
        summary = response.text.strip()

        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)