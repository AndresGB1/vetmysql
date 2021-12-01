from flask import Flask, render_template, redirect,url_for,request, flash
from .. import routes
from .. import mysql
from .color import *
from .raza import *


@routes.route('/vista_cliente/<string:username>/add_mascota', methods=['GET'])
def add_mascotau(username):
    if request.method == 'GET':
        return render_template('usuariot/add_mascotas.html', name=username)
    if request.method == 'POST':
        try:
            id_usuario = username
            id_raza = request.form['id_raza']
            id_color = request.form['id_color']
            nombre = request.form['nombre']
            sexo = request.form['sexo']
            peso = request.form['peso']
            fechaNacimiento = request.form['fechaNacimiento']
            estado = True;
            cur = mysql.connection.cursor()
            cur .execute("INSERT INTO mascota (id_usuario, id_raza, id_color, nombre, sexo, peso, fechaNacimiento, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id_usuario, id_raza, id_color, nombre, sexo, peso, fechaNacimiento, estado))
            mysql.connection.commit()
            flash('Mascota added successfully!')
            return redirect('') 
        except Exception as e:
            print('Error: ' + str(e))
            return redirect('/vista_cliente/<string:username>/add_mascota')

@routes.route('/vista_cliente/<string:username>/ver_mascotas', methods=['GET'])
def ver_mascotau(username):
    if request.method == 'GET':
        return render_template('usuariot/mascotas.html', name=username)


#get
@routes.route('/user/<string:username>/get_mascotas', methods=['GET'])
def get_mascotas(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mascota WHERE id_usuario = %s", [username])
    data = cur.fetchall()
    cur.close()
    return render_template('usuariot/mascotas.html', mascotas = data)

#get_by_id
@routes.route('/user/<string:username>/get_mascota/<string:id>', methods=['GET'])
def get_mascota(username, id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mascota WHERE id_usuario = %s AND id_mascota = %s", (username, id))
    data = cur.fetchall()
    return render_template('mascota/mascota.html', mascotas = data)