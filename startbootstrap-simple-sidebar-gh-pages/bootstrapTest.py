import flask
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#@app.route("/")
#def home():
 #   return render_template("index.html")


#if __name__ == "__main__":
 #   app.run(debug=True)

@app.route('/')
def index():
   #return render_template('index.html')  # this line only displays files in the templates sub directory.  To display from other directories, see below
   return flask.send_from_directory(".", path="index.html")
if __name__ == '__main__':
   app.run()