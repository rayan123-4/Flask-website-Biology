app = Flask(__name__)

@app.route("/testing")
def testing():
    user_name = "Rayan"
return render_template("testing.html", user_name=user_name)

