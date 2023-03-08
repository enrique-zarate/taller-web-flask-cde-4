from flask import Flask  # Importar el servidor
from flask import render_template # importar el render

app = Flask(__name__) # refiere al archivo actual

###### RUTAS ######
@app.route("/") # pagina principal
def pagina_de_inicio():
    return "Holis Bootcamp! desde Flask"

# Crear un ruta y tirarle HTML
@app.route("/saludo")
def saludo():
    return '''
    <h1>Hola desde CDE!</h1>
    <p>Bienvenidos al Bootcamp numero 4</p>
    '''

### Solucion de Giovanne
## RUTA2 ###
@app.route("/inicio")
def inicio():
    return render_template("domotica.html")

@app.route("/personaje/")
def personaje():
    datos_morty = {
        "nombre" : "Morty Sanchez",
        "descripcion" : "Muy miedoso",
        "ult_ubicacion" : "La Tierra",
        "url_imagen" : "https://pbs.twimg.com/profile_images/1095734111086538752/yo99K95N_400x400.png"
    } 
    return render_template("personaje.html", datos_morty_web=datos_morty)

# Programa que lea contenido de la URL
@app.route("/usuario/<nombre>/<contrasenha>")
def usuario(nombre, contrasenha):
    if nombre == "Enri" and contrasenha == "1234":
        return f"Bienvenido {nombre}"
    else:
        return f"Las credenciales no coinciden"
    


    


@app.route("/bienvenida/<nombre>")
def bienvenida(nombre):
    return f"Binevenido {nombre}"

###### CODIGO PARA LEVANTAR EL SERVIDOR #####
if __name__ == "__main__":
    app.run(debug=True)
