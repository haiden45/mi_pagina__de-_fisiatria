from flask import Flask, render_template, Response

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


# =========================
# SEO: robots.txt
# =========================
@app.route('/robots.txt')
def robots():
    contenido = """User-agent: *
Allow: /

Sitemap: https://mi-pagina-de-fisiatria.onrender.com/sitemap.xml
"""
    return Response(contenido, mimetype='text/plain')


# =========================
# SEO: sitemap.xml
# =========================
@app.route('/sitemap.xml')
def sitemap():
    contenido = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

    <url>
        <loc>https://mi-pagina-de-fisiatria.onrender.com/</loc>
    </url>

    <url>
        <loc>https://mi-pagina-de-fisiatria.onrender.com/emg</loc>
    </url>

    <url>
        <loc>https://mi-pagina-de-fisiatria.onrender.com/conduccion</loc>
    </url>

    <url>
        <loc>https://mi-pagina-de-fisiatria.onrender.com/potenciales</loc>
    </url>

    <url>
        <loc>https://mi-pagina-de-fisiatria.onrender.com/fisiatria</loc>
    </url>

    <url>
        <loc>https://mi-pagina-de-fisiatria.onrender.com/ondas</loc>
    </url>

</urlset>
"""
    return Response(contenido, mimetype='application/xml')


if __name__ == '__main__':
    app.run(debug=True)