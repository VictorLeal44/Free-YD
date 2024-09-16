import yt
from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__,template_folder="templates",static_url_path="/static")

titulo = "sin busqueda"
resultado = False

@app.route("/")
def index():
    return render_template("index.html", titulo=titulo, resultado=resultado)

@app.route("/ruta", methods=['POST','GET'])
def ruta():
    global url
    global titulo
    url = request.form.get("url")
    try:
        titulo = yt.nombre(url)
        print(url)
    except:
        titulo = "no se ha encontrado"
    return redirect(url_for("index"))

@app.route("/musica")
def musica():
    global resultado
    try:
        yt.musica(url)
        resultado = True
    except:
        resultado = False    
    return redirect(url_for("index"))

@app.route("/video/<formato>")
def video(formato):
    global resultado
    try:
        yt.video(url,formato)
        resultado = True
    except:
        resultado = False
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=2000,debug=True)