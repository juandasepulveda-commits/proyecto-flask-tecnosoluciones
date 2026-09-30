from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "cambia-esta-clave-en-produccion"

SERVICIOS = [
    {"nombre": "Desarrollo web", "descripcion": "Sitios y aplicaciones web a la medida con Python y Flask."},
    {"nombre": "Automatización", "descripcion": "Automatizamos tareas repetitivas para ahorrar tiempo y evitar errores."},
    {"nombre": "Análisis de datos", "descripcion": "Convertimos tus datos en tableros y reportes fáciles de entender."},
    {"nombre": "Ciberseguridad básica", "descripcion": "Buenas prácticas y revisión de seguridad para proteger tu información."},
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html", servicios=SERVICIOS)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip()
        mensaje = request.form.get("mensaje", "").strip()
        if nombre and correo and mensaje:
            flash(f"¡Gracias, {nombre}! Recibimos tu mensaje y te responderemos pronto.", "ok")
        else:
            flash("Por favor completa todos los campos.", "error")
        return redirect(url_for("contacto"))
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)
