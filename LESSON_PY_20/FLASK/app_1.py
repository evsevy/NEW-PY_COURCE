from flask import Flask, render_template, url_for

app = Flask(__name__)
menu = ["home", "contacts", "about"]
@app.route("/")
def index():
  print( url_for('index') )
  return render_template('index.html', title = "My first page", menu=menu)
  #  return "index"

if __name__ == "__main__":
    app.run(debug="True")