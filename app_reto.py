from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

def ecuacion_cuadratica(a,b,c):
    dis = (b**2)-(4 * a * c) #utilizar ** para elevar al cuadrado
    if dis>0.0:
        x1 = (-b + sqrt(dis)) / (2*a)
        x2 = (-b - sqrt(dis)) / (2*a)
        return x1, x2
    return 0,0

    
@app.route('/cuadratica', methods = ['POST'])
def calcular_funcion():
    data = request.get_json()
    input_A = data.get('a')
    input_B = data.get('b')
    input_C = data.get('c')
    #Iprimir dos valores de la funcion 
    result1,result2= ecuacion_cuadratica(input_A,input_B,input_C) 
        
         
    return jsonify({"X1 = ": result1,"X2":result2})


if __name__ == '__main__':
    app.run(debug=False)#paso 1. Cambiar a False