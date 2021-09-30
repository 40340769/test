from flask import Flask, request
app = Flask(__name__)

def hello():
    return "Hello"

hello = hello()

@app.route("/")
def root():
    return hello + "The default, 'root' route"

@app.route("/account/",methods=['GET','POST'])
def account():
    if request.method == 'POST':
        #return "POST'ed to /account root \n"
        print(request.form)
        name = request.form['name']
        return "Hello %s" % name
    else:
        #return "GET /account root \n"
        page = '''
        <html>
            <body>
                <form action="" method="post" name="form">
                    <label for="name">Name:</label>
                    <input type="text" name="name" id="name" />
                    <button id="submit" name="submit">Submit</button>
                </form>
            </body>
        </html>'''
        return page

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
