from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    titolo="Pagina iniziale"
    bottone="Info"
    testo="Hello World"
    return render_template("base.html", 
        titolo=titolo,
        testo=testo,
        bottone=bottone)

@app.route('/info')
def info():
    titolo="Pagina Info"
    bottone="Homepage"
    testo="Informazioni"
    return render_template("base.html", 
        titolo=titolo,
        testo=testo,
        bottone=bottone)

if __name__ == '__main__':
    app.run()
