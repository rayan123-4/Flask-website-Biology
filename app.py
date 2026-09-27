
from flask import Flask, render_template

app = Flask(__name__)

# The main home route (/)
@app.route("/")
def index():
    user_name = "Rayan"
    return render_template("index.html", user_name=user_name)

# The testing page route (/testing)
@app.route("/testing")
def testing():
    user_name = "Rayan"
    return render_template("testing.html", user_name=user_name)

if __name__ == "__main__":
    # Runs on port 8080 with auto-reload turned on!
    app.run(debug=True, port=8080)
