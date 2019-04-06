#Matheus Sado Nepomuceno Barros
#Ra:21803854

from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from m02 import *

app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'

@app.route('/')
def principal():
    cursor = mysql.get_db().cursor()
    return render_template('mainpage.html', professores = get_professores(cursor))

@app.route('/exibirProfessor/Matheus')
def exibirProfessor():
    cursor = mysql.get_db().cursor()
    return render_template('detailpage.html', Nome = 'Matheus', detalhes = get_detalhesM(cursor))

if __name__ == '__main__':
    app.run(debug=True)