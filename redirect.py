from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello - this is the main page"

@app.route("/private/")
def private():
    # Test for user logged in failed
    # so redirect to login URL
    return redirect(url_for("login"))

@app.route("/login/")
def login():
    return "Now we would get username & password"

#@app.route("/force500")
#def force500():
#    abort(500)

@app.errorhandler(404)
def page_not_found(error):
    return "Could not find the page you requested.",404

#@app.errorhandler(500)
#def error500(error):
#    return "Error 500 was forced.",500

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

