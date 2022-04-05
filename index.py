from flask import Flask, render_template, request, jsonify
from calculadora import Calculadora

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/calcular", methods=["GET", "POST"])
def calcular():

    requestData = request.form.keys()
    notHasNumber1 = "number1" not in requestData
    notHasNumber2 = "number2" not in requestData
    notHasOperation = "operation" not in requestData
    invalidParameters = notHasNumber1 or notHasNumber2 or notHasOperation
    if  invalidParameters:
        return "Missing parameters", 406
    

    number1 = int(request.form.get("number1"))
    number2 = int(request.form.get("number2"))
    operation = request.form.get("operation")

    calculadora = Calculadora(number1, number2)
    result = calculadora.calcular(operation)
    return str(result)

if __name__ == "__main__":
        app.run()