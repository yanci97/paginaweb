from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template('pagina.html')

@app.route('/servicio')
def servicio():
    return render_template('servicio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/sucursales')
def sucursales():
    return render_template('sucursales.html')
if __name__=='__main__':
    app.run(debug=True)
    

