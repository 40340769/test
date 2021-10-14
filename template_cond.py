from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name_p>")
@app.route("/hello/<name_p>/<club_p>")
def hello(name_p=None,club_p=None):
    user = {'name': name_p,'club': club_p}
    return render_template('conditional_1.html',user_t=user)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

