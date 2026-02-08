from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
todos = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.json
    todos.append({"task": data.get("task")})
    return {"message": "added"}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
