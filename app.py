from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/home')
def index():
    list_example = ["Alvin", "Simon", "Theodore"]
    return render_template("index4.html", list_example = list_example)
   # return render_template('index3.html')

if __name__ == '__main__':
    app.run()
