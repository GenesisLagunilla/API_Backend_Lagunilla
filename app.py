from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip().lower()

    if user_message == "hi":
        return "hello genesis"
    else:
        return "I didn't understand that."
    
    return jsonify({"reply": reply})
if __name__ == '__main__':
    app.run(debug=True,)
