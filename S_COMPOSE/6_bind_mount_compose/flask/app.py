import flask
from flask import request, json, jsonify
import requests
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Xrl10xde10'
app.config['MYSQL_DB'] = 'flaskdocker'

@app.route("/", methods=["GET"])
def index():
    data = requests.get('https://randomuser.me/api')
    return data.json()

@app.route("/inserthost", methods=['POST'])
def inserthost():
    data = requests.get('https://randomuser.me/api').json()

    for name in data['results']:
        username = (name['name']['first'])
        
    cur = mysql.connection.cursor()
    cur.execute("""INSERT INTO users(name) VALUES(%s)""", [(username,)])
    mysql.connection.commit()
    cur.close()

    return "usuário inserido: " + username

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")