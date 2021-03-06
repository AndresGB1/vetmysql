from flask import Flask
from rutas import routes
from database import mysql
import os


app =  Flask(__name__)
#Conexión a BD con archivo .env
app.config['MYSQL_USER'] = os.environ.get('USERDB') #'usuario'
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORDDB') #'password'
app.config['MYSQL_DB'] = os.getenv('DB') #'Base de datos'
app.config['MYSQL_HOST'] = os.getenv('HOSTDB') #'localhost'
app.secret_key = 'mysecretkey'

mysql.init_app(app)
app.register_blueprint(routes) #Registrar las rutas

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
