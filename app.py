from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def home():
    return render_template('home.html')

# Página EMG
@app.route('/emg')
def emg():
    return render_template('emg.html')

# Conducción nerviosa
@app.route('/conduccion')
def conduccion():
    return render_template('conduccion.html')

# Potenciales evocados
@app.route('/potenciales')
def potenciales():
    return render_template('potenciales.html')

# Fisiatría
@app.route('/fisiatria')
def fisiatria():
    return render_template('fisiatria.html')

# Ondas de choque
@app.route('/ondas')
def ondas():
    return render_template('ondas.html')

if __name__ == '__main__':
    app.run(debug=True)