from flask import Flask, render_template
app = Flask(__name__)

@app.route("/users/")
def display_clubs():
    clubs = ['Widzew','Bears','Milan','LFC']
    return render_template('collection_1.html',clubs_t=clubs)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

