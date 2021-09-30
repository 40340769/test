from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'route' route."

@app.route("/hello/")
def hello():
    return "Hello Napier!"

@app.route("/static-image/")
def static_image():
    start = '<img src="'
    url = url_for('static',filename='widzew.jpg')
    end = '" />'
    return start+url+end,200 

@app.route("/goodbye/")
def goodbye():
    return "Goodbye, see you later!"

@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested.",404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
