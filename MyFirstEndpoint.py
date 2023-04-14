# Importación de paquetes requeridos
#
from flask import Flask, jsonify

# Instanciación de una aplicación tipo flask
# 
app = Flask(__name__)

# Definición del endpoint tipo GET
#
@app.route('/', methods = ['GET'])
def index():
    return jsonify({'Mensaje':'Mi primer endpoint en Python'})

# Programa principal de Python
#
if __name__ == "__main__":
    app.run(debug = True)

