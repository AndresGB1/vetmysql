from flask import render_template, redirect,url_for,request, flash
from .. import routes
from database import mysql

@routes.route('/admin/<string:username>/get_historia/<id>/factura', methods=['GET'])
def factura(username,id):
    return render_template('administrador/factura.html',username=username ,id=id)

#Añadiendo una factura (id_historia id_pago fecha descuento total estado)
@routes.route('/admin/<string:username>/get_historia/<id>/add_factura', methods=['POST','GET'])
def add_factura(username,id):
    try:            
        if request.method == 'POST':
            id_historia = request.form['id_historia']
            id_pago = request.form['id_pago']
            fecha = request.form['fecha']
            descuento = request.form['descuento']
            total = request.form['total']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO factura(id_historia, id_pago, fecha, descuento, total, estado) VALUES (%s, %s, %s, %s, %s, %s)", (id_historia, id_pago, fecha, descuento, total, estado))
            mysql.connection.commit()
            flash('Factura creada correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar factura')
        print("No funciono ",e)
        return redirect('/')
#get_facturas
@routes.route('/cliente/agalvisb/ver_mascota', methods=['GET'])
def get_facturas():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM factura")
    facturas = cur.fetchall()
    cur.close()
    return facturas

