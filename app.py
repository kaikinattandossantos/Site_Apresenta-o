from flask import Flask, jsonify, render_template
import pyodbc

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html") 

@app.route("/competencias")
def competencias():
  return render_template("comp.html") 

@app.route("/projetos")
def projetos():
  return render_template("projetos.html") 

@app.route("/curriculo")
def curriculo():
  return render_template("curriculo.html") 

if __name__ == '__main__':
    app.run(debug=True)