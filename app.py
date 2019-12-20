from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    titolo="Pagina iniziale"
    bottone="Info"
    testo="Hello World"
    return render_template("base.html", testo=scritta)

@app.route('/info')
def info():
    titolo="Pagina Info"
    bottone="Homepage"
    testo="Hello World"
    testo="Informazioni"
    return render_template("base.html", testo=scritta)

if __name__ == '__main__':
    app.run()
