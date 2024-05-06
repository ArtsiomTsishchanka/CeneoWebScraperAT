from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/extract')
def index():
    return render_template("extract.html")

@app.route('/products')
def index():
    return render_template("products.html")

@app.route('/about')
def index():
    return render_template("about.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/product/<product_id>')
def name(name):
    return render_template("product.html", product_id=product_id)
