from flask import Flask, render_template, request, jsonify
from agent import run_agent

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("message", "").strip()
    
    if not user_input:
        return jsonify({"error": "الرسالة فاضية"}), 400
    
    result = run_agent(user_input)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)