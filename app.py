from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def home():
    name = request.args.get("name", "Guest")
    return f"Welcome {name}. Deployed via Portainer."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
