from flask import Flask, request
from flask import render_template

app= Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None

    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        estado = 'APROBADO' if promedio >= 40 and asistencia >= 75 else 'REPROBADO'

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    longitud_mayor = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        longitud_mayor = len(nombre_mayor)

    return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, longitud_mayor=longitud_mayor)

if __name__ == '__main__':
    app.run(debug=True)
