from flask import Flask, render_template, request
from jsonschema import ValidationError
from calculadora import Calculadora

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/calcular", methods=["GET", "POST"])
def calcular():

    try:

        requestData = request.form.keys()
        notHasNumber1 = "number1" not in requestData
        notHasNumber2 = "number2" not in requestData
        notHasOperation = "operation" not in requestData
        invalidParameters = notHasNumber1 or notHasNumber2 or notHasOperation
        if  invalidParameters:
            return "Missing parameters", 406

        operation = request.form.get("operation")
        number1 = int(request.form.get("number1"))
        number2 = int(request.form.get("number2"))

        calculadora = Calculadora()
        calculadora.setOperation(operation)
        calculadora.setNumber1(number1)
        calculadora.setNumber2(number2)
        return str(calculadora.calcular())


    except ValidationError as error:

        response = {
            "message": "Random ValidationError occured!"
        }

        if len(error.args) > 0:
            response["message"] = error.args[0]
        return response, 406
    
    except Exception as exception:

        response = {
            "message": "Random exception occured!"
        }

        if len(exception.args) > 0:
            response["message"] = exception.args[0]
        return response, 406


if __name__ == "__main__":
        app.run()