from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal: home.html como landing page
@app.route('/')
def home():
    return render_template('home.html')

# Ruta dinámica para usuario
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template('usuario.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)







