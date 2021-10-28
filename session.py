from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'ASbfgrty781!,?'

@app.route("/")
def index():
    return "Root of the session.py app."

@app.route("/session/write/<p_name>/")
def write(p_name=None):
    session['name'] = p_name
    return "Wrote %s into 'name' key of session" % p_name

@app.route("/session/read/")
def read():
    try:
        if(session['name']):
            return str(session['name'])
    except:
        pass
    return "No session variable set for 'name' key"

@app.route("/session/remove/")
def remove():
    session.pop('name',None)
    return "Removed key 'name' from session"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
        
