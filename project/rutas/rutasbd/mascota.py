from flask import Flask, render_template, redirect,url_for,request, flash
from .. import *


#Añadiendo id_usuario id_raza estado id_color nombre sexo peso fechaNacimiento
@routes.route('user/<id>/add_mascota', methods=['POST'])
def add_mascota():
    if(request.method == 'POST'):
        id_usuario = request.form['id_usuario']
        id_raza = request.form['id_raza']
        id_color = request.form['id_color']
        nombre = request.form['nombre']
        sexo = request.form['sexo']
        peso = request.form['peso']
        fechaNacimiento = request.form['fechaNacimiento']
        estado = True;
        cur = mysql.connection.cursor()
        cur .execute("INSERT INTO usuario (username, numeroDoc, nombres, apellidos, fechaNacimiento,pasword,sexo,direccion,correo,estado) VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,)", (username, numeroDoc, nombres, apellidos, fecha_nacimiento,password,sexo,direccion,correo,estado))  
        mysql.connection.commit()
        flash('User added successfully!');
        return redirect(url_for('Index'))

#edit
@routes.route('/user/<id>/edit_mascota/', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    return render_template('edit-user.html', contact = data[0])

#edit
@routes.route('/user/update/<id>', methods=['POST'])
def update_user(id):
    if request.method == 'POST':
        numeroDoc = request.form['numeroDoc']
        nombres = request.form['nombres']
        apellidos = request.form['appellidos']
        fecha_nacimiento = request.form['fecha_nacimiento']
        password = request.form['password']
        sexo = request.form['sexo']
        direccion = request.form['direccion']
        correo = request.form['correo']
        estado = True;
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET numeroDoc = %s,
                nombres = %s,
                apellidos = %s
                
            WHERE id = %s
        """)
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))
