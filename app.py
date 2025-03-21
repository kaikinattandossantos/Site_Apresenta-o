from flask import Flask, jsonify, render_template
import pyodbc

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html') 


@app.route('/sobremim')
def sobremim():
   return render_template('sobremim.html')


@app.route('/Competencias')
def competencias():
   return render_template('competencias.html')


@app.route('/Projetos')
def Projetos():
   return render_template('Projetos.html')



if __name__ == '__main__':
    app.run(debug=True)