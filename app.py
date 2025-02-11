from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Docker!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000) # Host 0.0.0.0 makes it accessible from outside the container
