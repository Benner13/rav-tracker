from flask import Flask, send_from_directory
app = Flask(__name__, static_folder=".")

@app.route("/")
def root():
    return send_from_directory(".", "index.html")

@app.route("/leaderboard.json")
def leaderboard():
    return send_from_directory(".", "leaderboard.json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
