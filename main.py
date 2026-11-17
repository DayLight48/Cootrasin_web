from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = "fjdsalfkjls"  # os.getenv("SECRET_KEY")
Bootstrap(app)

@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route('/quienes_somos')
def quienes_somos():
    return render_template("quienes_somos.html")


@app.route('/servicios')
def servicios():
    return render_template("servicios.html")


if __name__ == '__main__':
    app.run(debug=True)

