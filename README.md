# TecnoSoluciones – Prototipo web modular con Flask

Actividad 1 de **Fundamentos de programación web** (UNIMINUTO).
Aplicación web con tres páginas (Inicio, Servicios, Contacto) construida con Flask y Jinja2, usando una plantilla base con `{% extends %}`, `{% block %}` e `{% include %}`.

**Integrantes:** Juan David Sepúlveda · Juan Pablo Romero 

## Estructura

```
proyecto_flask/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── servicios.html
│   ├── contacto.html
│   └── includes/
│       ├── header.html
│       ├── navbar.html
│       └── footer.html
└── static/css/estilos.css
```

## Instalación y ejecución

Requisitos: Python 3.9 o superior.

1. Clonar el repositorio y entrar a la carpeta:
   ```bash
   git clone <URL-del-repositorio>
   cd proyecto_flask
   ```
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecutar la aplicación:
   ```bash
   python app.py
   ```
5. Abrir en el navegador: <http://127.0.0.1:5000>

## Cómo funciona la modularidad

- `base.html` define la estructura común y los bloques `{% block title %}` y `{% block content %}`.
- `header.html`, `navbar.html` y `footer.html` se insertan con `{% include %}` dentro de `base.html`.
- Cada página (`index`, `servicios`, `contacto`) extiende `base.html` y rellena sus bloques.
- Los estilos están en `static/css/estilos.css`.

## Referencias

- Adictos al trabajo. (2024). *Diseño y renderizado de páginas HTML en Python con Flask: guía completa.* https://adictosaltrabajo.com/2024/02/21/diseno-y-renderizado-de-paginashtml-en-python-con-flask-guia-completa/
- Pinto Demera, L. N., & Morejón López, G. E. (2025). FLASK: El microframework para el desarrollo rápido de aplicaciones con Python. *Revista Social Fronteriza, 5*(1), e597.
- Navarro, A. (2025). *Extensiones en Flask: Guía práctica.* Junco TIC. https://juncotic.com/extensiones-en-flask-guia-practica/
- LabEx. (2025). *Generando plantillas dinámicas y seguras con Jinja2.* https://labex.io/es/tutorials/flask-generating-secure-dynamic-templates-with-jinja2-188849
- Viera, U. (2025). *Guía completa de Jinja2 para desarrollo de plantillas en Python.* https://urianviera.com/python-flask/guia-completa-de-jinja2-para-el-desarrollo-deplantillas-en-python
