from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hi():
    return "Hello there"

@app.route("/hello/<name>")
def hello(name):
    return "Hello %s" % name

@app.route("/hello2/")
def hello2():
    name = request.args.get('name','')
    if name == '':
        return "no parameter supplied"
    else:
        return "Hello %s" % name   

@app.route("/add/<int:first>/<float:second>")
def add(first,second):
    return str(first+second)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
